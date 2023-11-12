
"""  
    THIS SCRIPT USE "relatedClasses" FUNCTION INCLUDED IN MyFunc (root path)

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback     
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

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")
        print(f"{FR_BLUE}=== MAIN")
        print("print empty line")
        print("=== display the relations of <Comercial> Class")
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

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        


else:
    # something wrong
    print(frRED("---- ******** ----"))
    