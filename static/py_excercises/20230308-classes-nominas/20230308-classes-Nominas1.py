"""  
    1.- This code is to pass the exercises to the teacher
    2.- Page 75 (nominas example)

"""
#
# IMPORT SECTION
#

try:   # Import My Own Functions from include dir 
    import os, sys, traceback, platform 
    from os.path import dirname, realpath
    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func
    from static.include.MyFunc import *
    from static.include.MyColors import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")


# CONSTANTS

# classes for this excercise
from Classes_Nomina import *

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

    try:
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

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

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    