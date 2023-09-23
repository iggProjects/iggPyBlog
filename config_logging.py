import datetime
import os, logging

basedir = os.path.abspath(os.path.dirname(__file__))

# error handling 
log_file_path = basedir + "/static/logFiles/server_messages.txt"
logging.basicConfig(filename=log_file_path, 
                encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)
