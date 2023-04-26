import sys
import subprocess
import progressbar

# Colors
NO_COLOR = "\033[00m"
FR_RED   = "\033[91m"
FR_GREEN = "\033[92m"
FR_YELL  = "\033[93m"
FR_BLUE  = "\033[94m"
FR_MAG   = "\033[95m"


# Draw spinner:
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

# Execute some job with multiple lines on stdout:
p = subprocess.Popen("python.exe z-worker.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Lines will be collected in list:
result = []

bar.start()

# Until I get last line and the end of string:
while p.stdout is not None:

    # Update spinner on one step:
    # It will update only when any line was printed to stdout!
    bar.update()
    # Read each line:

    line = p.stdout.readline()
    # Add line in list and remove carriage return

    result.append(line.decode('UTF-8').rstrip('\r'))

    # When no lines appears:
    if not line:
        print(f"\n\n{FR_BLUE}=== Leaving main loop !!! ==={NO_COLOR}\n\n")
        p.stdout.flush()
        break

    bar.update()


# Show finish message, it also useful because bar cannot start new line on console, why?
#print("Finished !")

# Print Results as string:
print(f"\nresult{''.join(result)}\n\n")