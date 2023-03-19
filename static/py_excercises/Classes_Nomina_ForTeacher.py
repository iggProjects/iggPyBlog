"""
    Classes for "nomina system"

    UML schema

     Empleado  ( id, nombre, año_ncto, dir_resid, cargo )                                                    
             ⇧
             |
             |
          extends
             |			
    SalarioEmpleado  ( + salario )                 ----->           SistemaNominas
             ⇧
             | calculo_nomina(): float                              calculo_nomina(): float
             |
          extends
             |			
    Comercial ( + comision_ventas )
             |  calculo_nomina(): float 

"""

# cleaning shell with system('cls')
from os import system 

# my generic functions
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

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

    def calculo_nomina(self):
        return self.salario

class Comercial(SalarioEmpleado):
    def __init__(self, id, nombre,año_ncto,dir_resid,cargo,salario,commision_ventas):
        super().__init__(id, nombre,año_ncto,dir_resid,cargo, salario)
        self.commision_ventas = commision_ventas

    def calculo_nomina(self):        
        fijo = super().calculo_nomina()
        return fijo + self.commision_ventas

# testing __mro__ built function
system('cls')

relatedClasses(Comercial)

