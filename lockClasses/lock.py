class Lock():
    def __init__(self, door, location,securitylevel):
        self.door=door
        self.location=location
        self.securitylevel=securitylevel
        self.status='locked'

    def setStatus(self, status):
        self.status=status

    def getStatus(self):
        return self.status

    def getDoor(self):
        return self.door

    def getLoction(self):
        return self.location

    def getSecurityLevel(self):
        return self.securitylevel

    def __str__(self):
        return str(self.door) + " " + self.status