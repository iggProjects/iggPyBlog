"""  
1.- This code is to pass the exercises to the teacher
2.- Musicians and instruments example

"""
#
# IMPORT SECTION
#
from MyFunc_ForTeacher import *
from Colors_ForTeacher import *

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":
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
            print(f"{FR_GREEN}{self.inst_name} is playing now{NO_COLOR}\n")

        def displayInfo(self):
            print(f"{FR_BLUE}Instrument {self.inst_name}:{NO_COLOR}\n\t--> type: {self.inst_type}, prize: {self.inst_prize}\n")            

    guitar=musicalInstruments("guitar", "cords", "100")
    guitar.play()
    guitar.displayInfo()

    class Pianos(musicalInstruments):
    #class Pianos(musicalInstruments(name, type_, prize)):        
        def __init__(self,inst_name,inst_type,inst_prize,inst_keys):
            super().__init__(inst_name,inst_type,inst_prize)
            self.inst_keys = inst_keys

        def displayPianosInfo(self):
            print(f"\n{FR_BLUE}Instrument {self.inst_name}:{NO_COLOR}\n\t--> type: {self.inst_type}, prize: {self.inst_prize}, keys: {self.inst_keys}{NO_COLOR}\n")            
    

    PianoCola = Pianos("Piano de Cola","cuerdas",1000,24)
    PianoCola.displayPianosInfo()

    class musicians(musicalInstruments):
        #(inst_name, inst_type, inst_prize)
        def __init__(self,musician_name,inst_name,inst_type,inst_prize):
            self.musician_name = musician_name
            super().__init__(inst_name,inst_type,inst_prize)
            
        def displayMusicianInfo(self):
            print(f"\n{FR_BLUE}{self.musician_name}{NO_COLOR}  plays with a {FR_GREEN}{self.inst_name}{NO_COLOR}\n")            

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
            print(f"\n{FR_BLUE}Musician {self.musician_name}, Instrument {self.inst_name}{NO_COLOR}\n")            

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

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()