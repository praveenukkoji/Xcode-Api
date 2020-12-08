from subprocess import run, PIPE
import uuid
import os


def getCppOutput(sourcecode, input):
    try:
        #TODO: handle mem exceed error
        filename = str(uuid.uuid4()).replace("-", "_") + '.cpp'

        with open(filename, 'w') as file:
            file.write(sourcecode)

        cmd = "g++ " + filename
        os.system(cmd)

        cmd = "rm " + filename
        os.system(cmd)

        if not os.path.isfile('a.out'):
            # TODO: check compilation error properly with stderr
            return "", "Compilation Error"

        sub_process = run(['gtimeout', '2s', './a.out'], stdout=PIPE, input=input, encoding='ascii')

        cmd = "rm " + './a.out'
        os.system(cmd)

        if sub_process.returncode == 0:
            #TODO: handle wrong answers here
            return sub_process.stdout, "Executed Successfully"
        elif sub_process.returncode == 124:
            return "", "Time Limit Exceeded"
        else:
            #TODO: check runtime error properly with stderr
            return "", "Runtime Error"
    except Exception as e:
        print(e)

    return "", "Unknown Error"

def getPythonOutput(sourcecode, input):
    pass

def getJavaOutput(sourcecode, input):
    pass