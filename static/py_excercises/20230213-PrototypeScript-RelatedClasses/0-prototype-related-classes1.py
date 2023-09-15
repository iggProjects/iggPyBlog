
"""  
    THIS SCRIPT USE "relatedClasses" FUNCTION INCLUDED IN MyFunc (root path)

"""
# IMPORT SECTION
import os, sys
from os import  system

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

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print("print empty line")
    print(f"{FR_BLUE}=== MAIN")
    print("print empty line")
    print("=== display the relations of 'Comercial' Class")
    print("print empty line")    

    #  Class Hierarchies
    class SistemaNominas:
        def calculo_nomina(self, empleados):
            for empleado in empleados:
                nomina_emp = '{:,.2f}'.format(empleado.calculo_nomina()).replace(',','.')
                print(f"{FR_GREEN}\t{empleado.nombre} ({empleado.id}) | cargo '{empleado.cargo}'{NO_COLOR}")
                print(f"\t\tpago: {nomina_emp} €")            

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
        
    class Comercial(SalarioEmpleado):
        def __init__(self, id, nombre,año_ncto,dir_resid,cargo,salario,commision_ventas):
            super().__init__(id, nombre,año_ncto,dir_resid,cargo, salario)
            self.commision_ventas = commision_ventas
        
    relatedClasses(Comercial)

    print("print empty line")    
    print(f"{FR_GREEN}=== That's all for today{NO_COLOR}")

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ----"))
    