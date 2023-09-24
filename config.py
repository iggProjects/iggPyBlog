"""

    basic configuration

"""

from flask import Flask, render_template, url_for, redirect, request, session
import os
import platform

# My Own Colors
from static.include.MyColors import *

# base dir in server
basedir = os.path.abspath(os.path.dirname(__file__))
#print(f"{FR_GREEN}==== basedir:{NO_COLOR}\n\t{basedir}")
# operating system in server
opSys = platform.system()
#print(f"{FR_YELL}==== OS:{NO_COLOR}\n\t{opSys}{NO_COLOR}")
# machine specifications
myMachine = platform.uname()
#print(f"{FR_BLUE}==== machine specif:{NO_COLOR}\n\t{myMachine}")

app = Flask(__name__)
app.secret_key = 'HI TARZAN'
