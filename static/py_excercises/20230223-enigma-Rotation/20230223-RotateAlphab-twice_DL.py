# IMPORT SECTION
# My Own Functions from include dir 
try:   # Import My Own Functions from include dir 
    import sys, traceback, string     
    from os import system
    from os.path import dirname, realpath
    # import My Own Func
    from MyColors import *
    from MyFunc_copy_DL import *    
except Exception as ImportError:
    FR_RED   = "\033[91m" 
    NO_COLOR = "\033[00m"
    print("print empty line") 
    print(f"{FR_RED}IMPORT ERROR ==>{NO_COLOR} {ImportError} | {ImportError.__class__} | {ImportError.__doc__}")

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]



if __name__ == "__main__":

    system('cls')

    # create list of alphabet
    string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    alphab = list(string.ascii_lowercase)
    print(f"{FR_YELL}\nORIGINAL ALPHABET LIST{NO_COLOR} (length: {len(alphab)})\n\t{str(alphab).replace(',','')}\n")

    # position to rotate list
    posit1 = int(input("Number to obtain first alphab list rotation? "))

    # print first and second terms
    print(f"\n{FR_GREEN}first and second terms{NO_COLOR}")
    print(f"\n{FR_YELL}alphab[ posit1 : ]{NO_COLOR}\n\t{str(alphab[posit1:])}" )
    print(f"\n{FR_YELL}alphab[ : posit1 ]{NO_COLOR}\n\t{str(alphab[:posit1])}" )

    alphab_01 = alphab[posit1:] + alphab[:posit1]
    # Printing list after left rotate
    #print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1}{NO_COLOR}\n\t{str(alphab_01).replace(',','')}" )
    print (f"\n{FR_YELL}First  alphabet after left rotate by {posit1} (formula: alphab[4:] + alphab[:4])\n\t{str(alphab_01).replace(',','')}{NO_COLOR}" )
    # position to rotate list
    posit2 = int(input("\nNumber to obtain second alphab list rotation ? "))

    alphab_02 = alphab_01[posit2:] + alphab_01[:posit2]
    # Printing list after left rotate
    print (f"\n{FR_YELL}Second alphabet after left rotate by {posit2}{NO_COLOR}\n\t{str(alphab_02).replace(',','')}\n" )
    pause()

    # back to Original using slicing to right rotate by 3
    orig_alphab = alphab_01[-posit1:] + alphab_01[:-posit1]
    
    # Printing after right rotate
    print (f"\n{FR_GREEN}Rotate back twice to return to the original alphabet{NO_COLOR}\n\t{str(orig_alphab).replace(',','')}\n")
    pause()

    # ------------------------------------------------
    #      IF YOU WANT, SHOW VARS CHARACTERISTICS 
    #------------------------------------------------- 
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
            pause()  

        except NameError:
            print(f"\n\t{FR_RED}---- Var '{_what_var}' doesn't exits 🙄🙄  ----")
            print(f"\n{FR_GREEN}--------------- That's all for today 👌 ---------------{NO_COLOR}\n")

    else:
        print(f"\n{FR_GREEN}---------- That's all for today 👌 ----------{NO_COLOR}\n")


else:
    # something wrong
    print(frRED("---- upsssssssss something is wrong ---"))
    pause()    