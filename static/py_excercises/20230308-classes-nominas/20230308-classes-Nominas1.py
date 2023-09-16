"""  
    1.- This code is to pass the exercises to the teacher
    2.- Page 75 (nominas example)

"""
#
# IMPORT SECTION
#

import os, sys

# cleaning shell with system('cls')
from os import system 

# include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
# check in what server is app
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *


# CONSTANTS

# my generic functions
from MyFunc import *

# classes for this excercise
from Classes_Nomina import *

# function
# checking related classes in a composite class 
def relatedClasses(clas):   

    print(f"----- analysis of {FR_BLUE} \"classes related\"{NO_COLOR} with class \"{FR_GREEN}{clas}{NO_COLOR}\" -----\n")
    for clas_rel in clas.__mro__:
        print(f"{FR_GREEN}\trelated clas --> {clas_rel}\n")
    print(f"{NO_COLOR}----- end analysis -----\n")    


#
# ---------- COURSE EXCERCISE ----------
#

#  Class Hierarchies
class SistemaNominas:
    def calculo_nomina(self, empleados):
        for empleado in empleados:
            nomina_emp = '{:,.2f}'.format(empleado.calculo_nomina()).replace(',','.')
            print(f"{FR_GREEN}\t\t{empleado.nombre} ({empleado.id}) | cargo '{empleado.cargo}'")
            print(f"\t\t\tImporte: {nomina_emp} euros")

class Empleado:    
    def __init__(self, id, nombre, año_ncto, dir_resid, cargo):
        self.id = id
        self.nombre = nombre
        self.año_ncto = año_ncto
        self.dir_resid = dir_resid
        self.cargo = cargo

class SalarioEmpleado(Empleado):
    def __init__(self, id, nombre,año_ncto,dir_resid,cargo,salario):
        super().__init__(id, nombre,año_ncto,dir_resid,cargo)
        self.salario = salario

    def calculo_nomina(self):
        return self.salario

class Comercial(SalarioEmpleado):
    def __init__(self, id, nombre,año_ncto,dir_resid,cargo,salario,commision_ventas):
        super().__init__(id, nombre,año_ncto,dir_resid,cargo, salario)
        self.commision_ventas = commision_ventas

    def calculo_nomina(self):        
        fijo = super().calculo_nomina()
        return fijo + self.commision_ventas

if __name__ == "__main__":
    
    print("print empty line")
    print(f"{FR_BLUE}===== MAIN =====")  
    print("print empty line")  

    # ------------------- Nominas excercise ------------------

    Empleados_empresa = []
    Empleados_empresa.append(SalarioEmpleado(1, 'Inaki','1959','Errenteria','programador html',1500))
    Empleados_empresa.append(SalarioEmpleado(2, 'Xabier','1990','Donostia','programador java',1700))
    Empleados_empresa.append(SalarioEmpleado(3, 'Pedro', '1965','Donosita','programador python',2000))  

    Comerciales_empresa = []
    Comerciales_empresa.append(Comercial(4, 'Che','1980','Bilbo','ventas empresas grandes',2500, 250,))
    Comerciales_empresa.append(Comercial(5, 'Oihana','1985','New York','staff marketing',3500, 500))

    print(f'\t{FR_BLUE}======= Calculando Nomina General ========')
    print("print empty line")

    corrida_nomina = SistemaNominas()    

    print(f"{FR_BLUE}\t\t=== Grupo Oficinas ===")
    corrida_nomina.calculo_nomina(Empleados_empresa)
    print("print empty line")
    print(f"{FR_BLUE}\t\t=== Grupo Comerciales ===")
    corrida_nomina.calculo_nomina(Comerciales_empresa)

    print("print empty line")
    print(f"\t{FR_BLUE}======= Fin Corrida Nomina Empresa =======")   
    
    print("print empty line")
    
    # relatedClasses(Comercial)
    print(f"\t{FR_BLUE}=== Analysis of related classes for {Comercial} ===")
    
    for clas_rel in Comercial.__mro__:
        print(f"{FR_GREEN}\t\trelated clas --> {clas_rel}\n")
    print("print empty line")

    print(f"{FR_BLUE}===== That's All =====")
    print("print empty line")    


else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    