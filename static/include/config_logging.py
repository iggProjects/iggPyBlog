import logging

#basedir = os.path.abspath(os.path.dirname(__file__))
from config import basedir

# error handling 
log_file_path = basedir + "/static/logFiles/server_messages.txt"
logging.basicConfig(filename=log_file_path, 
                encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)

"""
# create dir & logFiles for logging process
static_path = dirname(dirname(__file__))
logDirPath = os.path.join(static_path, 'logFiles')
if os.path.exists(logDirPath):
    pass
else:
    os.makedirs(logDirPath)
log_file_path = logDirPath + "/server_messages.txt"
logging.basicConfig(filename=log_file_path, 
                encoding='utf-8', level=logging.DEBUG, format="%(asctime)-15s %(levelname)-8s %(funcName)s %(message)s")
logging.captureWarnings(True)
"""