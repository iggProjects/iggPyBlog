"""
            😎  My colors for printing  😎
"""
# https://www.geeksforgeeks.org/print-colors-python-terminal/
# colored text and background 

# FOREGORUND CONSTANTS
FG_RED          = 91
FG_GREEN        = 92
FG_YELLOW       = 93
FG_LIGHT_PURPLE = 94
FG_PURPLE       = 95
FG_CYAN         = 96
FG_LIGHT_GRAY   = 97
FG_BLUE         = 34   # ???
FG_BLACK        = 98

NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[34m"


# BACKGROUND CONSTANTS
BG_BLACK  = 16
BG_BLUE   = 17
BG_RED    = 124
BG_ORANGE = 165

# foreground functions
def prRed(msg):         print("\033[91m{}\033[00m".format(msg)) 
def prGreen(msg):       print("\033[92m{}\033[00m".format(msg)) 
def prYellow(msg):      print("\033[93m{}\033[00m".format(msg)) 
def prLightPurple(msg): print("\033[94m{}\033[00m".format(msg)) 
def prPurple(msg):      print("\033[95m{}\033[00m".format(msg)) 
def prCyan(msg):        print("\033[96m{}\033[00m".format(msg)) 
def prLightGray(msg):   print("\033[97m{}\033[00m".format(msg)) 
def prBlue(msg):        print("\033[34m{}\033[00m".format(msg)) 
def prBlack(msg):       print("\033[98m{}\033[00m".format(msg)) 

# FOREGROUND CONSTANTS FOR PRINT FUNCTION
def frGREEN(msg):  return f"\033[92m{msg} \033[00m"   # green
def frRED(msg):  return f"\033[91m{msg} \033[00m"   # red

# PRINT FUNCTIONS

# foreground
def prFG(msg,col):
    col1 = str(col)
    return print(("\033[" + col1 + "m " + msg + " \033[0;0m\n"))

# background
def prBG(msg,col):
    col1 = str(col)
    return print(("\033[48;5;" + col1 + "m " + msg + " \033[0;0m\n"))
    #return(f"\033[48;5;{col1}m {col1} \033[0;0m\n".format(msg))

def prBG_orange(msg): 
    return print(("\033[48;2;255;165;0m {} \033[0;0m".format(msg)))

