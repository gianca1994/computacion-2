import os
from constants import ResponseCode


class Commands:

    @staticmethod
    def ls():
        try:
            return ResponseCode.OK_CODE + "\n".join(os.listdir())
        except:
            return ResponseCode.ERROR_CODE

    @staticmethod
    def pwd():
        try:
            return ResponseCode.OK_CODE + os.getcwd()
        except:
            return ResponseCode.ERROR_CODE

    @staticmethod
    def cd(argument):
        try:
            os.chdir(argument)
            return ResponseCode.OK_CODE + os.getcwd()
        except:
            return ResponseCode.ERROR_CODE + ResponseCode.COMMAND_FAIL
