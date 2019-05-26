'''
class that stores a door a card number 
for permission--going to ignore time
data and other features for now.
'''
class Permission():
    def __init__(self, door, card):
        self.door=door
        self.card=card

    def getDoor(self):
        return self.door

    def getCard(self):
        return self.card