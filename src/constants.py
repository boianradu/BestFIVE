class CONSTANTS:
    """CONSTANTS is a singleton class that stores the CONSTANTS
    used by app """
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if CONSTANTS.__instance == None:
            CONSTANTS()
        return CONSTANTS.__instance

    def defineConstants(self):
        self.SIZE_HEIGHT=720
        self.SIZE_WIDTH=1280

    def __init__(self):
        """ Virtually private constructor. """
        self.defineConstants()
        if CONSTANTS.__instance != None:
            raise Exception("This class is a CONSTANTS!")
        else:
            CONSTANTS.__instance = self

        