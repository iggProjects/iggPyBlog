import time
import random

# CONSTANTS
# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"

print(f"\n{FR_BLUE}START SOMETHING{NO_COLOR}\n")

for i in range(4):
    sec = random.randint(1, 3)
    print("\tSleeping for: %d seconds" % sec)
    time.sleep(sec)
    print(f"\t\t{FR_GREEN}Making job, line: %d{NO_COLOR}" % i)

print(f"\n{FR_BLUE}END SOMETHING{NO_COLOR}")