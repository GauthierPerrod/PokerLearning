''' class responsible of the organising the game and setting the rules'''
import player
import utils
import random
from card import Card

class Ruler:
    def __init__(self, nb_comp=8, nb_hplayer=0, starting_cash=20000, big_blind=200):
        self.players = None
        self.starting_cash=starting_cash
        self.big_blind=big_blind
        self.deck= self.init_deck()
    def init_deck(self):
        self.deck=[]
        for i in ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']:
            for j in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                self.deck.append(Card(i,j))
        random.shuffle(self.deck)
        return(self.deck)



if __name__ == "__main__":
    ruler=Ruler()
    print(ruler.deck)
