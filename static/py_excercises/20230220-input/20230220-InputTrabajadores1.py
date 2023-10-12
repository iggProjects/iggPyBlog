# scrip for register worker data

# IMPORT
try:   # Import My Own Functions from include dir 
    import re
    import platform
    from math import ceil
    import sys, traceback, json
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
    print("print empty line") 


# MAIN
if __name__ == "__main__":

    try:
        # clear console screen
        clear_console_screen()
        # get name of script
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        print("print empty line")
        print(f"{FR_BLUE}=== MAIN ==={NO_COLOR}")
        print("print empty line")
        print(f"{FR_GREEN}=== INPUT WORKERS TABLE{NO_COLOR}")
        print("print empty line")
         
        # argument dict
        workers = json.loads(sys.argv[1])
        
        print(f"\n\t{FR_YELL}Session terminated by user{NO_COLOR}\n")        
        print(f"\tVar Workers type: {type(workers)} | Values: {workers}\n")
       
        print("print empty line") 
        """       
        for k in workers:
            print(f"\t\tName: {k} | age: {workers[k]}")        
        """
        for i in range(len(workers)):
            print(f"\tworker {i}: - {workers[i]}, type: {type(workers[i])}")        
            print(f"\t\tName: {workers[i][0]} | Age: {workers[i][1]}")

        print("print empty line")
        print(f"\n{FR_GREEN}---------- That's all for today ----------{NO_COLOR}\n")     

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)  

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    
