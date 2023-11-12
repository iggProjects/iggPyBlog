"""  
1.- This code is to pass the exercises to the teacher
2.- Musicians and instruments example

"""
#
# IMPORT SECTION
#
try:   # Import My Own Functions from include dir 
    import os, sys, traceback
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

        print(f"{FR_GREEN}---------- main ----------")

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")

        # my code

        class musicalInstruments:
            def __init__(self, inst_name,inst_type,inst_prize):
                self.inst_name = inst_name
                self.inst_type = inst_type
                self.inst_prize = inst_prize
                self.__inst_cost = inst_prize*0,8

            def play(self):
                print(f"{FR_GREEN}--->{self.inst_name} is playing now")

            def displayInfo(self):
                print(f"{FR_YELL}----> Instrument {self.inst_name}")
                print(f"{NO_COLOR}---------> type: {self.inst_type}, prize: {self.inst_prize}")            

        guitar=musicalInstruments("Guitar", "cords", "100")
        guitar.play()
        guitar.displayInfo()

        class Pianos(musicalInstruments):
        #class Pianos(musicalInstruments(name, type_, prize)):        
            def __init__(self,inst_name,inst_type,inst_prize,inst_keys):
                super().__init__(inst_name,inst_type,inst_prize)
                self.inst_keys = inst_keys

            def displayPianosInfo(self):
                print(f"{FR_YELL}Instrument {self.inst_name}")
                print(f"----> type: {self.inst_type}, prize: {self.inst_prize}, keys: {self.inst_keys}")            
        

        PianoCola = Pianos("Piano de Cola","cuerdas",1000,24)
        PianoCola.displayPianosInfo()

        class musicians(musicalInstruments):
            #(inst_name, inst_type, inst_prize)
            def __init__(self,musician_name,inst_name,inst_type,inst_prize):
                self.musician_name = musician_name
                super().__init__(inst_name,inst_type,inst_prize)
                
            def displayMusicianInfo(self):
                print(f"\t{FR_YELL}{self.musician_name} plays with a {FR_GREEN}{self.inst_name}")            

        Beethoven = musicians("Ludwig van Beethoven","Piano", "Cuerdas", 20000 )
        Beethoven.displayMusicianInfo()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(f"{FR_RED}---- ******** ----")
    