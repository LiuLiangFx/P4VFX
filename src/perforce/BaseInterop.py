import tempfile

class BaseInterop(object):
    @staticmethod
    def main_parent_window():
        raise NotImplementedError

    @staticmethod
    def createMenu(entries):
        raise NotImplementedError

    @staticmethod
    def getIconPath():
        raise NotImplementedError
    
    @staticmethod
    def getSceneFiles():
        return []
    
    @staticmethod
    def getTempPath():
        return tempfile.gettempdir()

    @staticmethod
    def getCurrentSceneFile():
        raise NotImplementedError

    @staticmethod
    def openScene(filePath):
        raise NotImplementedError

    @staticmethod
    def closeWindow(ui):
        raise NotImplementedError

    @staticmethod
    def refresh():
        raise NotImplementedError