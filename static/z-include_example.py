
"""  
THIS SCRIPT IS FOR PRINTING WITH COLORS

"""
# IMPORT SECTION

# get name of script
my_script = __file__.split('\\')
my_script_name = my_script[len(my_script)-1]

# import "My Own Funct" from root path
# from MyFunc import *

try: 
    from include import MyColors1
except Exception as ImportError:   
    print(f"IMPORT ERROR ==> {ImportError}")    
#
# ---------- MAIN ----------
#

if __name__ == "__main__":

    try:

        print(f"IN 'z-include_example'")
        print("print empty line")

        print(f"{MyColors1.FR_GREEN}---------- MAIN ----------{MyColors1.NO_COLOR}")
        print("print empty line")

        print(f"---------- using CONTANTS for colors ----------")
        print("print empty line")

        colors= [MyColors1.FR_RED,MyColors1.FR_GREEN,MyColors1.FR_YELL,MyColors1.FR_BLUE,MyColors1.FR_MAG]
        colors_str=['\\033[91m - Red','\\033[92m - Green','\\033[93m - Yellow','\\033[94m - Blue','\\033[95m - Magenta']
        
        i=0
        for color in colors:
            color_str = color
            msg=" ==> TESTING COLOR FUNCTION"
            msg = msg.rjust(30)
            #print("MyColors1.FR_RED value: " + colors_str[0])
            print("\tPrint with ascii " + colors_str[i] + f":\t{color}{msg}") 
            i+=1  
        msg="print with default color:\t\t ==> TESTING COLOR FUNCTION"
        print(f"\t{msg}")   
        print("print empty line")
    
        print(f"{MyColors1.FR_GREEN}---------- That's all for today ----------{MyColors1.NO_COLOR}")

    except Exception as Argument:
        error_msg = "ERROR IN <" + my_script_name + "> !"
        print(f"ERROR {error_msg}")        
        print(f"exception as Argumment: {Argument} | {Argument.__class__} | {Argument.__doc__}")        
        
    
else:
    # something wrong
    print(MyColors1.frRED("---- upsssssssss something is wrong ----"))

