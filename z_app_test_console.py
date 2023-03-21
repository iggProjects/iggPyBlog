from flask import Flask

app_test_console = Flask(__name__)


@app_test_console.route('/')
def run_script_cmdLine():
    
    file = open(r'testing_execution_file.bat', 'r').read()    
    #file = open(r'static\\py_excercises\\20230227\\20230227-OS-Dir-Files-Example_For_Teacher.py', 'r').read()    
    return exec(file)

    #import os
    #os.system('cls')
    #os.system('cmd /c "static\\py_excercises\\20230227\\z-openCmdLine-20230227-OS-Dir-Files.py"')

    #return "<center>upsssss i do not understand</center>"


if __name__ == "__main__":
    app_test_console.run(debug=True)