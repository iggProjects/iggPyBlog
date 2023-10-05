"""  
    1.- This code is to pass the exercises to the teacher
    2.- Page 75 (nominas example)

"""
#
# IMPORT SECTION
#

# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

# classes for this excercise
from Classes_Nomina_DL import *

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
    
    # clean screen
    system('cls')
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # ------------------- Nominas excercise ------------------

    Empleados_empresa = []
    Empleados_empresa.append(SalarioEmpleado(1, 'Iñaki','1959','Errenteria','programador html',1500))
    Empleados_empresa.append(SalarioEmpleado(2, 'Xabier','1990','Donostia','programador java',1700))
    Empleados_empresa.append(SalarioEmpleado(3, 'Pedro', '1965','Donosita','programador python',2000))  

    Comerciales_empresa = []
    Comerciales_empresa.append(Comercial(4, 'Che','1980','Bilbo','ventas empresas grandes',2500, 250,))
    Comerciales_empresa.append(Comercial(5, 'Oihana','1985','New York','staff marketing',3500, 500))

    print(f'\n{FR_YELL}======= Calculando Nómina General ========{NO_COLOR}\n')
    
    corrida_nomina = SistemaNominas()    

    print(f"\n\t{FR_YELL}=== Grupo Oficinas ==={NO_COLOR}\n")
    corrida_nomina.calculo_nomina(Empleados_empresa)

    print(f"\n\t{FR_YELL}=== Grupo Comerciales ==={NO_COLOR}\n")
    corrida_nomina.calculo_nomina(Comerciales_empresa)

    print(f"{FR_GREEN}\n======= Fin Corrida Nómina Empresa =======\n{NO_COLOR}")   
    pause()

    print(f"\n{FR_YELL}See related classes for \"Comercial\" object{NO_COLOR}\n\n")

    relatedClasses(Comercial)
    pause()

    # ------------------------------------------------
    #          SHOW VARS CHARACTERISTICS 
    #------------------------------------------------ 
    yesss=True   
    while yesss:
        _msg = "Do you want to see attributes for a specific VAR ? (Y,N): "
        answer=Y_N_2(_msg)        
        if answer in ['Y','N']: yesss = False

    if answer == 'Y':            
        # add question for name of var.....
        _what_var = str(input("What VAR ? "))
        try: 
            _what_var
            _my_Obj_name = eval(_what_var)
            print(f"\n{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------{NO_COLOR}\n")
            pause()
            # my objects functions  
            mostrar(_my_Obj_name)  
            pause()     

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")
            pause()

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()