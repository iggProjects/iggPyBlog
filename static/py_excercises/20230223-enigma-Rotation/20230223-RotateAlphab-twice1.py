# IMPORT SECTION
try:   # Import My Own Functions from include dir 
    import sys, traceback, string     
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

if __name__ == "__main__":
        
    try:
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")
        # create list of alphabet
        string.ascii_lowercase
        'abcdefghijklmnopqrstuvwxyz'
        alphab = list(string.ascii_lowercase)
        print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n{alphab}\n")
        print("print empty line")

        # position to rotate list
        posit1 = 4
        #posit1 = int(input("Position to obtain first alphab list rotation? "))

        alphab_01 = alphab[posit1:] + alphab[:posit1]
        # print first and second terms
        print(f"\n{FR_GREEN}first and second terms{NO_COLOR}")
        print(f"\n{FR_YELL}alphab[ 4 : ]{NO_COLOR}\n\t{str(alphab[posit1:])}" )
        print(f"\n{FR_YELL}alphab[ : 4 ]{NO_COLOR}\n\t{str(alphab[:posit1])}" )
        print("print empty line")

        # Printing list after left rotate
        print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1} (formula: alphab[4:] + alphab[:4])\n\t{str(alphab_01)}{NO_COLOR}" )
        print("print empty line")

        # position to rotate list
        posit2 = 5
        #posit2 = int(input("\nPosition to obtain second alphab list rotation ? "))

        alphab_02 = alphab_01[posit2:] + alphab_01[:posit2]
        # Printing list after left rotate
        print (f"\n{FR_YELL}Second alphabet after left rotate by {posit2}{NO_COLOR}\n{str(alphab_02)}\n" )
        print("print empty line")
        #pause()

        # back to Original using slicing to right rotate by 3
        orig_alphab = alphab_01[-posit1:] + alphab_01[:-posit1]
        
        # Printing after right rotate
        print (f"\n{FR_GREEN}Rotate back twice to return to the original alphabet{NO_COLOR}\n{str(orig_alphab)}\n")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info(Argument,traceback,my_script_name)        

else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ---"))
    