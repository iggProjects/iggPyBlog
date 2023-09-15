
"""  
    THIS SCRIPT USE "relatedClasses" FUNCTION INCLUDED IN MyFunc (root path)

    EXECUTE ONLY IN LOCALHOST
"""
# IMPORT SECTION
import os, sys
from os import  system

# Include root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)
sys.path.insert(1, ROOT_DIR)

# Import My Own Funct in root path
from MyFunc import *

# CONSTANTS

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    system('cls')

    print(frGREEN("\n---------- main ----------\n"))
    print(frGREEN("\n--------------- display the relations of class 'Comercial' --------------\n"))
    pause()

    #  Class Hierarchies
    class SistemaNominas:
        def calculo_nomina(self, empleados):
            for empleado in empleados:
                nomina_emp = '{:,.2f}'.format(empleado.calculo_nomina()).replace(',','.')
                print(f"{FR_GREEN}\t{empleado.nombre} ({empleado.id}) | cargo '{empleado.cargo}'{NO_COLOR}\n\t\tpago: {nomina_emp} €\n")            

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
    pause()

    print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")

    # ------------------------------------------------
    #           ASKING FOR SHOW VARS INFO 
    #------------------------------------------------- 
    """
    # with Y_N_2 function
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
            #_my_Obj_name = None 

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")
    """
else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong 😢😢  ----\n"))
    pause()