
"""  
    THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION

# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        # clear console screen
        import platform
        clear_console_screen()
        
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print()

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print()
        pause()

        print(f"---------- using CONTANTS for colors ----------")
        print()
        
        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=1/0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1  
        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")   
        print()

        print(frGREEN(f"---------- using function prRed(msg) ----------"))         
        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print()
        prRed(msg)   
        print()
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        pause()

    except Exception as Argument:        
        write_traceback_info(Argument,traceback,my_script_name)        
        pause()

else:
    # something wrong
    print(frRED("---- ****** ----"))
