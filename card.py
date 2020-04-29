''' Class responsible of the main brick of poker : a card. 
A card as a value e.g : ten, and  a color e.g : spade'''


class Card:
    def __init__(self, value=None, color=None):
        self.value = value
        self.color = color
    # Method to print the value of the card    
    def __str__(self):
        return(str(self.value) + " of " + str(self.color))

    def __repr(self):
        return( "Card:"+ str(self.value) + " of " + str(self.color))
    # Overriding '=='
    def __eq__(self, other): 
        return (self.__dict__ == other.__dict__)
    

    
if __name__ == "__main__":
    card = Card('Jack', 'Spades')
    print(card)
    card_2 = Card('Jack', 'Spades')
    card_3 = Card('Jack', 'Hearts')
    card_4 = Card('Ten', 'Clubs')
    card_5 = Card('Eight', 'Diamonds')
    print(card==card_2)
    print(card==card_3)

    print(card==card_4)
    print(card==card_5)

