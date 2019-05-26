from lock import Lock
import datetime

class Scan():
    def __init__(self, door, location, securitylevel, card):
        self.lock=Lock(door,location,securitylevel)
        self.card=card
        self.scantime=datetime.datetime.now()
    
    def getLock(self):
        return self.lock
    
    def getCard(self):
        return self.card

    def getScanTime(self):
        return self.scantime
