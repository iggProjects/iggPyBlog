
"""  
    THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION

try:   # Import My Own Functions from include dir 
    import sys, traceback     
    from os.path import dirname, realpath
    from os import scandir
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
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        # https://www.geeksforgeeks.org/python-program-to-get-the-file-name-from-the-file-path/
        # https://www.w3docs.com/snippets/python/getting-a-list-of-all-subdirectories-in-the-current-directory.html
        # https://unix.stackexchange.com/questions/602346/what-can-i-use-to-get-the-paths-of-all-parent-directories-for-a-given-path

        # get all subdirs in path
        """
        subdir = []

        for item in os.listdir():
            if os.path.isdir(item):
                subdir.append(item)

        print(subdir)        
        
        subdirs = [x[0] for x in os.walk(dirname(__file__))]
        #subdirs = [x[0] for x in os.walk('.')]
        for subdir in subdirs:
            print(subdir)  
        print(f"os.scandir: {os.scandir(dirname(__file__))}")
        subfolders= [f.path for f in os.scandir(dirname(__file__)) if f.is_dir()]
        for dir in list(subfolders):
            print(f"dir: {dir}")
    
        print(type(os.walk(__file__)))
        """
        # get name of script
        #my_script = os.path.split(__file__)
        #my_script = os.path(__file__).split('/')
        #my_script = os.path.basename(__file__).split('/')[-1]
        #print(f"......my_script: {my_script}")
        my_script = __file__.split('\\')
        my_script_name = my_script[len(my_script)-1]
        #print(f".....my_script_name: {my_script_name}")
        print()
        write_log_file("my_messages.txt","IN '" + my_script_name + "'")
        print("print empty line")

        print(f"{FR_GREEN}---------- MAIN ----------{NO_COLOR}")
        print("print empty line")

        print(f"---------- using CONTANTS for colors ----------")
        print("print empty line")

        colors= [FR_RED,FR_GREEN,FR_YELL,FR_BLUE,FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1  
        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")   
        print("print empty line")

        print(frGREEN(f"---------- using function prRed(msg) ----------"))         
        msg="\tprint with function pfRed(msg) --> TESTING COLOR FUNCTION"
        print("print empty line")
        prRed(msg)   
        print("print empty line")
        
        print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")
        print("print empty line")        

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + ">. SEE server_messages.txt !"
        write_log_file("my_messages.txt",error_msg)
        write_traceback_info_1(Argument,traceback,my_script_name)        
    
else:
    # something wrong
    print(frRED("---- ******** ----"))
