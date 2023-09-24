"""

    basic configuration

"""

from flask import Flask, render_template, url_for, redirect, request, session

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
from static.include.MyColors import *

# base dir in server
basedir = os.path.abspath(os.path.dirname(__file__))
print(f"{FR_GREEN}==== basedir: {basedir}{NO_COLOR}")

# operating system in server
opSys = platform.system()
print(f"{FR_YELL}==== OS: {opSys}{NO_COLOR}")

# machine specifications
myMachine = platform.uname()
print(f"{FR_MAG}==== machine specif:{NO_COLOR}")
print(f"\t{myMachine}")

app = Flask(__name__)
app.secret_key = 'HI TARZAN'
