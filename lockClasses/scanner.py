'''
Creates a scan and passes it off to be validated
if the validation returns true
then it unlocks the door
else it leaves it locked
'''
from scan import Scan
from validate import Validator
from lock import Lock

class Scanner():
    def __init__(self, scan):
        self.scan=scan

    def validateScan(self):
        v=Validator()
        result=v.validate(self.scan)
        if result==True:
            self.scan.lock.setStatus('unlocked')
        else:
            self.scan.lock.setStatus('locked')
        