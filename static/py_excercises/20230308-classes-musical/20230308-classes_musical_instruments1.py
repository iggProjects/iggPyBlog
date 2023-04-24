"""  
1.- This code is to pass the exercises to the teacher
2.- Musicians and instruments example

"""
#
# IMPORT SECTION
#
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
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    system('cls')
    print(f"{FR_GREEN}---------- main ----------")
    

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


else:
    # something wrong
    print(f"{FR_RED}---- upsssssssss something is wrong ----")
    