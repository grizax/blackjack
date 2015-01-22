class Card:
    """
    Creates a card with a given suit/value and prints card
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def printcard(self):
        return self.value
