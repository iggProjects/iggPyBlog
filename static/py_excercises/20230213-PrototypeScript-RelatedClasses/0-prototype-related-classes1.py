
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
from MyFunc import *
from MyColors import *
from os import  system

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

#
# ---------- MAIN ----------
#

if __name__ == "__main__":


    print("\n---------- main ----------\n")
    print("\n--------------- display the relations of class 'Comercial' --------------\n")
    

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

    print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")

else:
    # something wrong
    print(frRED("\n---- upsssssssss something is wrong ----\n"))
    