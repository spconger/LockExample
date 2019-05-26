import unittest
from lock import Lock
from scan import Scan


class LockTest(unittest.TestCase):
    def setUp(self):
        self.lock=Lock(3176,'be','normal')

   
    def test_lockString(self):
        self.assertEqual(str(self.lock),'3176 locked')
    
    def test_securityLevel(self):
        self.assertEqual(str(self.lock.getSecurityLevel()),'normal')

    def test_SetStatus(self):
        self.lock.setStatus('unlocked')
        self.assertEqual(self.lock.getStatus(), 'unlocked')

    def test_GetDoor(self):
        self.assertEqual(str(self.lock.getDoor()), '3176')

    def test_GetLocation(self):
        self.assertEqual(self.lock.getLoction(), 'be')

class ScanTest(unittest.TestCase):
    def setUp(self):
        self.scan=Scan(3176, 'be', 'normal','123')

    def test_getLock(self):
        lock = self.scan.getLock()
        self.assertEqual(str(lock.getDoor()), '3176')

    def test_getScanTime(self):
        time = self.scan.getScanTime()
        self.assertEqual(self.scan.getScanTime(), time)

    def test_getCard(self):
        self.assertEqual(str(self.scan.getCard()), '123')
    
    
