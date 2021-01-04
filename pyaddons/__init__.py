def log(statment, filePath="logger.log"):
    print(statment)
    with open(filePath,'a') as file:
        file.write("\n\t\t" + statment)

class logger:

    filePath = ""
    file = None
    timeWritten = False
    defaultAction = ""

    def __init__(self, filePath="logger.log",default="l"):
        self.filePath = filePath
        self.defaultAction = default
    
    def openFile(self,mode="a"):
        self.file = open(self.filePath, mode)

    def closeFile(self):
        self.file.close()

    def log(self,statment,code=None):
        if code == None:
            code = self.defaultAction
        printTrue = False
        logTrue = False
        typeAdded = False
        printStatment = ""
        for char in code:
            if char == "p":
                printTrue = True
            elif char == "l":
                logTrue = True
            elif char == "e":
                statment = "[ERROR]\t" + statment
                typeAdded = True
            elif char == "w":
                statment = "[WARN]\t" + statment
                typeAdded = True
        
        if typeAdded == False:
            printStatment = statment
            statment = "\t\t" + statment
            
        if not printTrue and not logTrue:
            if self.defaultAction == "pl":
                printTrue = True
                logTrue = True
            elif self.defaultAction == "p":
                printTrue = True
            else:
                logTrue = True

        if logTrue:
            if not self.timeWritten:
                import datetime
                try:
                    self.openFile("r")
                    fileContents = self.file.read()
                    self.closeFile()
                except FileNotFoundError:
                    fileContents = ''

                self.openFile()
                if fileContents != '':    
                    self.file.write("\n\n")
                date = datetime.datetime.now()
                self.file.write("------- %s/%s/%s %s:%s:%s --------"%(date.strftime("%d"),date.strftime("%m"),date.strftime("%Y"),date.strftime("%H"),date.strftime("%M"),date.strftime("%S")))
                self.file.close()
                self.timeWritten = True
            self.openFile()
            self.file.write("\n")
            self.file.write(statment)
            self.closeFile()
        if printTrue:
            if typeAdded: print(statment)
            else: print(printStatment)

        return statment

def getOS():
    import sys
    platforms = {
    'linux1' : 'linux',
    'linux2' : 'linux',
    'darwin' : 'mac',
    'win32' : 'win32'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]