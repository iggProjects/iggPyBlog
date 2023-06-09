"""  
1.- This code is to pass the exercises to the teacher
2.- The SCRIPT is for:
    2.1.-
    2-2.-
    .
    .

"""
#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
from math import ceil
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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
    pause()

    # my code
    # page 71
    print(f"\n-------------------users-----------------------\n")

    class User:
        def __init__(self, name, mobile, age):
            self.name = name
            self.mobile = mobile
            self.age = age

        def __eq__(self,other):
            return self.name == other.name \
                and self.mobile == other.mobile \
                    and self.age == other.age

        def __str__(self):
            return f"\tname:{self.name}, "\
                f"age:{self.age}, "\
                f"mobile:{self.mobile}"


    user_1 = User("Jon","111",20)
    user_2 = User("Igg","222",20)

    print(f"{FR_GREEN}some operations with 'Users' Object\n{NO_COLOR}")
    print(f"\t{user_1.age}")    
    print(f"\t{user_1==user_2}")
    print(f"{user_1.__str__()}")

    # -------------------perros-----------------

    print(f"\n-------------------perros-----------------------\n")

    class Perro:

        def __init__(self, nombre, edad, raza):
            self.nombre = nombre
            self.edad = edad
            self.raza = raza

    perros =[] 

    miles = Perro("Miles", 4, "Jack Russell Terrier")
    buddy = Perro("Buddy", 9, "Dachshund")
    jack = Perro("Jack", 3, "Bulldog")
    jim = Perro("Jim", 5, "Bulldog")

    perros.append(miles)
    perros.append(buddy)
    perros.append(jack)
    perros.append(jim)

    print(f"{FR_GREEN}perros object list:{NO_COLOR}\n")
    matrix_view(perros,1)
    print()

    print(f"{FR_GREEN}perros details:{NO_COLOR}\n")
    for p in perros:
        print(f"\tEl perro se llama {p.nombre} y es {p.raza}")

    print()    

    # -------------------Superhero-----------------
    print(f"\n-----------------Superhero---------------------\n")

    class Superhero:
        def __init__(self, name):
            self.__name = name

        def displayname(self):
            print("Hero:", self.__name, "\n")

    myHeroe = Superhero("Shaktiman")

    # in this case, printing proceeds
    myHeroe.displayname()

    # in this case, we will have an error
    print(f"{FR_GREEN}\tIN THIS CASE, we will have an error ==> {FR_YELL}\"myHeroe.__name can't be invoked\"{NO_COLOR}\n")
    print(myHeroe.__name)


    
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