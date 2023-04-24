"""  
    1.- This code is to pass the exercises to the teacher
    2.- Page 75 (nominas example)

"""
#
# IMPORT SECTION
#

# cleaning shell with system('cls')
from os import system 

# my generic functions
from MyFunc import *
from MyColors import *

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

# classes for this excercise
from Classes_Nomina import *

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    
    print(f"{FR_GREEN}---------- main ----------")
    

    # ------------------- Nominas excercise ------------------

    Empleados_empresa = []
    Empleados_empresa.append(SalarioEmpleado(1, 'Iñaki','1959','Errenteria','programador html',1500))
    Empleados_empresa.append(SalarioEmpleado(2, 'Xabier','1990','Donostia','programador java',1700))
    Empleados_empresa.append(SalarioEmpleado(3, 'Pedro', '1965','Donosita','programador python',2000))  

    Comerciales_empresa = []
    Comerciales_empresa.append(Comercial(4, 'Che','1980','Bilbo','ventas empresas grandes',2500, 250,))
    Comerciales_empresa.append(Comercial(5, 'Oihana','1985','New York','staff marketing',3500, 500))

    print(f'{FR_YELL}======= Calculando Nómina General ========')
    
    corrida_nomina = SistemaNominas()    

    print(f" ===> {FR_YELL}=== Grupo Oficinas ===")
    corrida_nomina.calculo_nomina(Empleados_empresa)

    print(f" ===> {FR_YELL}=== Grupo Comerciales ===")
    corrida_nomina.calculo_nomina(Comerciales_empresa)

    print(f"{FR_GREEN}======= Fin Corrida Nómina Empresa =======")   
    

    print(f"{FR_YELL}See related classes for \"Comercial\" object")     
    relatedClasses(Comercial)
    


else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    