from execute.utils import getCppOutput, getPythonOutput, getJavaOutput
from execute.constants import cpp, python3, java


class OnlineCompiler:

    def __init__(self, request):
        self.request = request

    def getOutput(self):
        payload = ""
        try:
            sourcecode = self.request.get('sourcecode', None)
            input = self.request.get('input', None)
            filetype = self.request.get('filetype', None)

            if not (sourcecode and input and filetype):
                return "", "Missing Parameters"

            if filetype == cpp:
                payload, message = getCppOutput(sourcecode, input)
            elif filetype == python3:
                payload, message = getPythonOutput(sourcecode, input)
            elif filetype == java:
                payload, message = getJavaOutput(sourcecode, input)
        except Exception as e:
            print(e)

        return payload, message

