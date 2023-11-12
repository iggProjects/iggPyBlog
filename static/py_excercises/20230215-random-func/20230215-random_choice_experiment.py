"""  
    Testing reliability of the random function

    We will make a thousand executions of the random function in the interval 1 to 10 to verify the probability that a certain number will come out

    EXECUTE ONLY IN LOCALHOST

"""
#
# IMPORT SECTION
#
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback, random
    import platform
    from os import system
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


#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    try:

        # clear console screen
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]

        print(f"\n\t{FR_GREEN}---------- main ----------{NO_COLOR}\n")
        print(f"An experiment to check random function, simulating a 'dice'")
        print()
        pause()
        
        my_dice = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

        ideal_perc = (1/6)
        ideal_dice = {'1':ideal_perc,'2':ideal_perc,'3':ideal_perc,'4':ideal_perc,'5':ideal_perc,'6':ideal_perc}
        face_list=list(range(1,7))
        print(f"\tDICE faces: {face_list}")
        print()
        pause()

        for i in range(1,21):
            iterations = 6000 * 2 * i
            #print("my_value: " + my_value)
            for i in range(iterations):        
                face = random.choice(face_list)
                my_dice[str(face)] += 1        

            print(frGREEN(f"\n\tExperiment result with {iterations} dice rolls:\n"))
            #print(frGREEN(f"\n\tExperiment result with {iterations:,d} dice rolls:\n"))
            for key in my_dice:
                #face_perc = "{:.4f}".format(100*(dice[key]/iterations))
                ideal_dice = int( ideal_perc * iterations)
                #ideal_dice = int( (ideal_perc/100) * iterations)
                face_diff = my_dice[key] - ideal_dice
                face_diff_perc = "{:.4f}".format(100 * (face_diff / iterations))
                #face_diff = str(face_diff).center(5)
                face_diff = str(face_diff).rjust(6,' ')
                face_diff_perc = str(face_diff_perc).rjust(8,' ')
                print(f"\t{key}: my dice: {my_dice[key]} | ideal dice: {ideal_dice} | diff: {face_diff} ({face_diff_perc}%) ")
            
            # reset my_dice dict values
            my_dice = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}   

            print()

        print(f"\t{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")

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
    print(f"\n{FR_RED}---- ******** ---{NO_COLOR}\n")
    pause()