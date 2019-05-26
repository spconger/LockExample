from permission import Permission
from validate import Validator
from scan import Scan
from scanner import Scanner

class RunScan():
    def __init__ (self):
        self.val = Validator()
        self.run()
                

    """ def setPermissions(self):
        p1=Permission(3176, 123)
        p2=Permission(3178, 123)
        p3=Permission(3172, 234)
        p4=Permission(3312, 234)

        self.val.addPermission(p1)
        self.val.addPermission(p2)
        self.val.addPermission(p3)
        self.val.addPermission(p4) """

    def setScan(self):
        self.scan=Scan(3176,'BE','Normal',123)

    def setScanner(self):
        self.scanner=Scanner(self.scan)

    def getValidation(self):
        self.scanner.validateScan()

    def run(self):
        print("setting permissions")
        #self.setPermissions()
        print ("setting up scan")
        self.setScan()
        print(self.scan.lock)
        print("sending scan to validator")
        self.setScanner()
        self.getValidation()
        
        print("the door is " + self.scan.lock.getStatus())


