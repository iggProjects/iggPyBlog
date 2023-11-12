"""  
    
    THIS SCRIPT IS FOR .............

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback, string, random, time, datetime
    import numpy as np   
    from os.path import dirname, realpath
    from os import scandir
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
    print() 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# ---------- CONSTANTS & FUNCTIONS ----------


NUM_ALPHAB = 200000

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

# place thousands separator
def place_comma(numb):
    # thousands separated with dot
    return format(numb,',d').replace(",",".")
    #return ("{:.}".format(numb))

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        clear_console_screen()

        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print()

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print()

        # at {datetime.now()}
        # time
        inicio = time.time()
        system('cls')
        
        print(f"\n{FR_GREEN}=== MAIN ==={NO_COLOR}\n")
        print(f"{FR_GREEN}=== process generating permutations of \'abcdefghijklmnopqrstuvwxyz\' start at {datetime.datetime.now()}\n")

        alphab_26 = 'abcdefghijklmnopqrstuvwxyz'
        alphab_26_list = list(alphab_26)
        numb_alphab = 0
        alphab_with_char_conflict = 0
        num_chars_equal = 0

        # delete if exists  
        if os.path.exists(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt"):
            os.remove(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt")
            print(f"\told z-permutFile.txt deleted")    

        if os.path.exists(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFileSorted.txt"):
            os.remove(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFileSorted.txt")
            print(f"\told z-permutFileSorted.txt deleted")    


        while numb_alphab < NUM_ALPHAB:
        
            alp = list(alphab_26)
            random.shuffle(alp)
            
            # discard permutations that keep the character in place
            for i in range(26):
                if alp[i] == alphab_26_list[i]:
                    #print(f"\t{i+1}: {''.join(alp)} | {''.join(alphab_15_list)}")
                    num_chars_equal +=1
            #print()       

            if num_chars_equal == 0:
                alp = ''.join(alp)
                alp = alp + '\n'
                permutFile = open(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt", "a")
                #permutFile = open("z-permutFile.txt", "a")
                permutFile.write(alp)
                permutFile.close()
                numb_alphab += 1
            else:
                alphab_with_char_conflict += 1    

            num_chars_equal = 0              
        
        # delete duplicated lines and sort
        uniqlines = set(open(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt").readlines())
        #uniqlines = set(open('z-permutFile.txt').readlines())
        uniqlines = sorted(uniqlines)
        #print(f"uniqlines type is {type(uniqlines)}")
        open(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFileSorted.txt", 'w').writelines(uniqlines)
        #open('z-permutFileSorted.txt', 'w').writelines(uniqlines)

        # delete z-permutFile.txt
        if os.path.exists(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt"):
            os.remove(basedir + "/static/proj_enigmaGame_scripts/temp/z-permutFile.txt")
            print(f"\t== z-permutFile.txt deleted\n")   

        # time  
        elapsed_time = (time.time()-inicio)
        #elapsed_time = "{:..2f}".format(time.time()-inicio)
        alphab_per_seconds = (numb_alphab + alphab_with_char_conflict)/(time.time()-inicio)
        alphab_per_seconds_format = place_comma(int(alphab_per_seconds))
        #alphab_per_seconds_format = "{:,.2f}".format(alphab_per_seconds)

        print(f"\n{FR_GREEN}\tNumber of new alphabets in z-permutFileSorted.txt:{NO_COLOR} {place_comma(numb_alphab)}\n")
        print(f"\n{FR_GREEN}\tTotal alphabets discarded by conflict in character position:{NO_COLOR} {place_comma(alphab_with_char_conflict)}\n")
        print(f"\n{FR_GREEN}=== process generating alphabets stoped at {datetime.datetime.now()}{NO_COLOR}\n")
        print(f"\n{FR_GREEN}===  Elapsed time in seconds:{NO_COLOR} {str(elapsed_time).replace('.',',')}\n")
        
        print(f"\n{FR_GREEN}===  Total Alphabets per Seconds:{NO_COLOR} {alphab_per_seconds_format}\n\n")
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        print()
        pause()

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)
        pause()     

else:
    # something wrong
    print(f"\n{FR_RED}---- ***********  ---{NO_COLOR}\n")
    pause()