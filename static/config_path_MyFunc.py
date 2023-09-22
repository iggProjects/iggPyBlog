import os, sys

# include real root path in sys.path
ROOT_DIR = os.path.abspath(os.curdir)

# check in what server is app, and add "prefix"
if "iggWebNz" in ROOT_DIR:              # pythonanywhere  
    ROOT_DIR = ROOT_DIR + "/mysite"
else:                                   # working in localhost server
    pass 
sys.path.insert(1, ROOT_DIR)

# import "My Own Funct" from root path
from MyFunc import *

