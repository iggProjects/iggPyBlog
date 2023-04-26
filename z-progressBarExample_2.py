import sys
import subprocess
import progressbar
import time
from time import sleep
from os import system

# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

system('cls')

print(f"progressbar.UnknownLength: {dir(progressbar.UnknownLength)}\n")
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
bar.start()

# Registro hora-seg inicio
inicio = time.time()

print(f"\n{FR_BLUE}=== inicio: min {time.localtime().tm_min}, sec {time.localtime().tm_sec} ==={NO_COLOR}")
print(f"\t{FR_GREEN}type of var '.tm_sec' {type(time.localtime().tm_sec)}{NO_COLOR}\n")

running=True
while running:    

    #
    # code
    #

    if time.localtime().tm_sec == 5:
        print(f"\n\n{FR_MAG}=== time expired at\n{time.localtime()}! ==={NO_COLOR}\n") 
        running = False
        #break

    bar.update()

ahora = time.time()
ahora = time.time()
print(f"\t{FR_RED}=== elapsed time: {ahora-inicio} ==={NO_COLOR}")    