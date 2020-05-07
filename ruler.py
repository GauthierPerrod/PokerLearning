''' class responsible of the organising the game and setting the rules'''
import utils
import random
from card import Card
from rounds import Round
from player import Player

class Ruler:
    def __init__(self, nb_comp=8, nb_hplayer=0, starting_cash=20000, big_blind=200):
        self.players = None
        self.playing_players = None
        self.starting_cash=starting_cash
        self.big_blind=big_blind
        self.deck= self.init_deck()
        self.rounds = Round(0)
    def init_deck(self):
        self.deck=[]
        for i in ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']:
            for j in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                self.deck.append(Card(i,j))
        random.shuffle(self.deck)
        return(self.deck)
    def playing_loop(self):
        while self.playing_players > 0:
            1+1


if __name__ == "__main__":
    ruler=Ruler()
    print(ruler.deck)
