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
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

# classes for this excercise
from Classes_Nomina_ForTeacher import *

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

    print(f'\n{FR_BLUE}======= Calculando Nómina General ========{NO_COLOR}\n')
    
    corrida_nomina = SistemaNominas()    

    print(f"\n\t{FR_BLUE}=== Grupo Oficinas ==={NO_COLOR}\n")
    corrida_nomina.calculo_nomina(Empleados_empresa)

    print(f"\n\t{FR_BLUE}=== Grupo Comerciales ==={NO_COLOR}\n")
    corrida_nomina.calculo_nomina(Comerciales_empresa)

    print(f"{FR_GREEN}\n======= Fin Corrida Nómina Empresa =======\n{NO_COLOR}")    


    
    
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

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()