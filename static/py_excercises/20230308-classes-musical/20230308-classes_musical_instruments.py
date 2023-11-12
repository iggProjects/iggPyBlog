"""  
1.- This code is to pass the exercises to the teacher
2.- Musicians and instruments example

"""
#
# IMPORT SECTION
#
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
    import platform 
    from os.path import dirname, realpath
    from os import system
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

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
        
    try:

        # clear console screen
        clear_console_screen()
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")
        pause()

        # my code

        class musicalInstruments:
            def __init__(self, inst_name,inst_type,inst_prize):
                self.inst_name = inst_name
                self.inst_type = inst_type
                self.inst_prize = inst_prize
                self.__inst_cost = inst_prize*0,8

            def play(self):
                print(f"\t{FR_GREEN}{self.inst_name} is playing now{NO_COLOR}")

            def displayInfo(self):
                print(f"\t\t{FR_YELL}Instrument {self.inst_name}:{NO_COLOR}\n\t\t--> type: {self.inst_type}, prize: {self.inst_prize}\n")            

        guitar=musicalInstruments("Guitar", "cords", "100")
        guitar.play()
        guitar.displayInfo()

        class Pianos(musicalInstruments):
        #class Pianos(musicalInstruments(name, type_, prize)):        
            def __init__(self,inst_name,inst_type,inst_prize,inst_keys):
                super().__init__(inst_name,inst_type,inst_prize)
                self.inst_keys = inst_keys

            def displayPianosInfo(self):
                print(f"\t{FR_YELL}Instrument {self.inst_name}:{NO_COLOR}\n\t\t--> type: {self.inst_type}, prize: {self.inst_prize}, keys: {self.inst_keys}{NO_COLOR}\n")            
        

        PianoCola = Pianos("Piano de Cola","cuerdas",1000,24)
        PianoCola.displayPianosInfo()

        class musicians(musicalInstruments):
            #(inst_name, inst_type, inst_prize)
            def __init__(self,musician_name,inst_name,inst_type,inst_prize):
                self.musician_name = musician_name
                super().__init__(inst_name,inst_type,inst_prize)
                
            def displayMusicianInfo(self):
                print(f"\t{FR_YELL}{self.musician_name}{NO_COLOR} plays with a {FR_GREEN}{self.inst_name}{NO_COLOR}\n")            

        Beethoven = musicians("Ludwig van Beethoven","Piano", "Cuerdas", 20000 )
        Beethoven.displayMusicianInfo()

        """class musicalTeam(musicians,Pianos):
        #class musicalTeam(musicians(musician_name),Pianos(inst_name, inst_type, inst_prize, inst_keys)):

            #def __init__(self):
            def __init__(self,musician_name,inst_name,inst_type,inst_prize,inst_keys):
                #super().__init__(musician_name,inst_name)
                self.musician_name = musicians(musician_name)
                self.inst_name = Pianos(inst_name)
                self.inst_type = Pianos(inst_type)
                self.inst_prize = Pianos(inst_prize)
                self.inst_keys = Pianos(inst_keys)           

            def displayMusicalTeam(self):
                print(f"\n{FR_YELL}Musician {self.musician_name}, Instrument {self.inst_name}{NO_COLOR}\n")            

        Beethoven_Piano = musicalTeam(Beethoven,PianoCola)
        Beethoven_Piano.displayMusicalTeam()"""

            
        
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

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"\n{FR_RED}---- ******** ----{NO_COLOR}\n")
    pause()