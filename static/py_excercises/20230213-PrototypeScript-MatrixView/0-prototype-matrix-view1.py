
"""  
THIS SCRIPT IS FOR..................

"""
# IMPORT SECTION
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
# ---------- MAIN ----------
#

if __name__ == "__main__":

    print(f"{FR_GREEN}---------- main ----------{NO_COLOR}")    

    sqr_var = [i*i for i in range(100)]

    print(f"{FR_BLUE}---------- list of first hundred numbers squared ----------{NO_COLOR}")

    matrix_view(sqr_var,20)
 
    print(f"{FR_GREEN}---------- That's all for today ----------{NO_COLOR}")

else:
    # something wrong
    print("---- upsssssssss something is wrong ----")
    