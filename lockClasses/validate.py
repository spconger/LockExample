'''
validates the scan against
a list of permissions
in this case hard coded, but would
be read from a database
'''
from scan import Scan
from permission import Permission

class Validator():
    def __init__(self):
        
        self.permissions=[]
        
    
    def addPermission(self,permission):
        self.permissions.append(permission)

    def validate(self, scan):
        p1=Permission(3176, 123)
        p2=Permission(3178, 123)
        p3=Permission(3172, 234)
        p4=Permission(3312, 234)

        self.addPermission(p1)
        self.addPermission(p2)
        self.addPermission(p3)
        self.addPermission(p4)

        door = scan.lock.getDoor()
        card=scan.getCard()
        
        result=False
        for p in self.permissions:
            if p.door==door and p.card==card:
                result=True
                break
       
        return result
                
    
    