"""

    basic configuration

"""

from flask import Flask, render_template, url_for, redirect, request, session
# LoginManager

from flask_sqlalchemy import *
import os
import platform
import sys

# handling data and time var's
import datetime

# error handling
import traceback
import logging

# My Own Colors
from MyColors import *

# base dir in server
basedir = os.path.abspath(os.path.dirname(__file__))
print(f"{FR_GREEN}............ basedir ===> {basedir}{NO_COLOR}")

# operating system in server
opSys = platform.system()
print(f"{FR_YELL}............ OS ===> {opSys}{NO_COLOR}")

# machine specifications
myMachine = platform.uname()
#print(f"==== host name: {myMachine}")

#print(f"globals: {type(globals())}\n{globals()}")

# log messages
logging.basicConfig(filename=basedir + "/static/logFiles/server_messages.log", 
                    encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)
#logging.captureWarnings(False)

# My Own Funct
from MyFunc import *

app = Flask(__name__)
app.secret_key = 'HI TARZAN'
#app.config['APPLICATION_ROOT'] = os.path.abspath(os.path.dirname(__file__))
#print(f"app config : {app.config['APPLICATION_ROOT']}")
