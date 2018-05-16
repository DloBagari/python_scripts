""" context manager.. make back up for file """
import os
class Updating:
    def __init__(self, filename):
        self.__filename = filename

    def __enter__(self):
        try:
            self.__backup = self.__filename+"_backup"
            os.rename(self.__filename, self.__backup)
        except FIleNotFoundError:
            # file not exist so no backup
            self.__backup = None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            try:
                os.rename(self.__filename, self.__filename+"_error")
            except FileNotFoundError:
                pass
            if self.__backup:
                os.rename(self.__backup, self.__filename)
                
