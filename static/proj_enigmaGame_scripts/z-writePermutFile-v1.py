#
# IMPORT SECTION
#
from MyFunc import *
from MyColors import *
from os import system
import string, random, time

#
# ---------- COURSE EXCERCISE ----------
#

if __name__ == "__main__":

    # time
    inicio = time.time()
    system('cls')
    print(f"\n{FR_GREEN}---------- main ----------{NO_COLOR}\n")

    alphab = 'abcdefghijklmnopqrstuvwxyz'

    # create file copy z-permutFile.txt
    #permutFile = open("z-permutFile.txt", "w")
    #permutFile.write('Jelouuuuu....\n')
    # write list of random permutations of alphab 
    # create list of alphabet

    numb_alphab = 0
    alphab_repeated = 0
    #permutFile = open("z-permutFile.txt", "w")

    for i in range(10):
        alp = list(alphab)
        random.shuffle(alp)
        alp = ''.join(alp)
        #alp = ''.join(random.choices(string.ascii_lowercase, k=26))

        with open(r'z-permutFile.txt', 'r') as file:
            # read all content from a file using read()
            content = file.read()
            # check if string present or not
            if alp in content:
                exists = 1
                #print('\tstring exist')
            else:
                exists = 0
                #print('\t\tstring does not exist')
                #print(f"{FR_GREEN}\tnew alphab permut:{NO_COLOR} {alp}\n")
        
        if exists == 0:
            permutFile = open("z-permutFile.txt", "a")
            alp = alp+'\n'
            permutFile.write(alp)
            #permutFile.close()
            numb_alphab += 1
            #print(f"\t{numb_alphab}")
        else:
            permutFile.write('repetido\n')    
            alphab_repeated =+ 1 

        permutFile.close()

    """
    # reading permutations file
    f = open("z-permutFile.txt","r")
    print(f"{FR_GREEN}\nprinting alphab permut {f.name}{NO_COLOR}\n")

    # read lines
    lines = f.readlines()
    for line in lines:  
        print(f"\t{line}")
    f.close()
    """
    # time  
    elapsed_time = "{:.2f}".format(time.time()-inicio)
    print(f"\n{FR_GREEN}\tTotal new alphabets generated: {numb_alphab}{NO_COLOR}\n")
    print(f"\n{FR_GREEN}\tTotal alphabets repeated during creation process: {alphab_repeated}{NO_COLOR}\n")
    print(f"\n================  Elapsed time: {elapsed_time}  =================\n\n")
    

else:
    # something wrong
    print(f"\n{FR_RED}---- upsssssssss something is wrong 😢😢  ---{NO_COLOR}\n")
    pause()