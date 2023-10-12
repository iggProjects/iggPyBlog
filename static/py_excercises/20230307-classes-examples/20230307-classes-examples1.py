"""  
1.- This code is to pass the exercises to the teacher
2.- The SCRIPT is for:
    2.1.-
    2-2.-
    .
    .

"""
# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
    import platform
    from os.path import basename, dirname, isdir, isfile, realpath
    from zipfile import ZipFile
    from os import system
    from pathlib import Path

    # get parent up 2 from __file__ path: 'static path'   
    up2_dir = dirname(dirname(dirname(realpath(__file__))))
    # insert path in sys.path
    sys.path.append(up2_dir)
    # get parent up 3 from __file__ path: 'static parent path'       
    up3_dir = dirname(dirname(dirname(dirname(realpath(__file__)))))
    # insert path in sys.path
    sys.path.append(up3_dir)
    # import My Own Func    
    from static.include.MyColors import *
    from static.include.MyFunc import *
    #from static.include.MyFunc_copy_DL import *
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
        
    try:

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print("print empty lines")    
        print(f"{FR_GREEN}---------- main ----------")
        print("print empty lines")    

        # my code
        # page 71
        print(f"-------------------users-----------------------")

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

        print(f"{FR_GREEN}some operations with 'Users' Object")
        print(f"\t{user_1.age}")    
        print(f"\t{user_1==user_2}")
        print(f"{user_1.__str__()}")

        # -------------------perros-----------------

        print(f"-------------------perros-----------------------")

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

        print(f"{FR_GREEN}perros object list:")
        matrix_view(perros,1)
        print()

        print(f"{FR_GREEN}perros details:")
        for p in perros:
            print(f"\tEl perro se llama {p.nombre} y es {p.raza}")

        print()    

        # -------------------Superhero-----------------
        print(f"-----------------Superhero---------------------")

        class Superhero:
            def __init__(self, name):
                self.__name = name

            def displayname(self):
                print("Hero:", self.__name, "")

        myHeroe = Superhero("Shaktiman")

        # in this case, printing proceeds
        myHeroe.displayname()

        # in this case, we will have an error
        print(f"{FR_GREEN}\tIN THIS CASE, we will have an error ==> {FR_YELL}\"myHeroe.__name can't be invoked\"")
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
                print(f"{FR_GREEN}---------- INFO FOR OBJECT '{_my_Obj_name}' ----------")
                
                # my objects functions  
                mostrar(_my_Obj_name)       

            except NameError:
                print(f"\t{FR_RED}---- Var '{_what_var}' doesn't exits ----")
                print(f"{FR_GREEN}--------------- That's all for today ---------------")

        else:
            print(f"{FR_GREEN}---------- That's all for today ----------")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        


else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    