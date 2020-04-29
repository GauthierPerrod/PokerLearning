''' Class responsible for the actions of a player.
A player has an absolute position around the table, a starting hand composed of 2 dealt cards, a given value of chips, 
and a number of states possible, e.g: dealt, flop, turn, river, call, bet, raise, fold, allin'''

class Player:
    def __init__(self, absoluteposition, state, firstcard, secondcard, chipsvalue):
        self.absoluteposition = absoluteposition
        self.state = state
        self.firstcard = firstcard
        self.secondcard = secondcard
        self.chipsvalue = chipsvalue
    #Method to print the dealt hand of the player
    def __str__(self):
        return('position : ' + str(self.absoluteposition) + "\n"
        'state : ' + str(self.state) + "\n"
        ' dealt hand : ' + str(self.firstcard) + " & "+ str(self.secondcard) + "\n"
        'chips value : ' + str(self.chipsvalue))
    def __repr__(self):
        return('Position around the table : ' + str(self.absoluteposition) + "\n"
        'State : ' + str(self.state) + "\n"
        'Dealt Hand : ' + str(self.firstcard) + ' & ' + str(self.secondcard) +"\n"
        'Chips Value : ' + str(self.chipsvalue))
    #Override
    def __eq__(self, other):
        return(self.__dict__ == other.__dict__)

if __name__ == "__main__":
    player0 = Player("0", "dealt", "Seven of Spades", "Two of Hearts", 1000)
    print(player0)
    player1 = Player("1", "dealt", "Jack of Spades", "Ten of Clubs", 1000)
    player2 = Player("0", "dealt", "Seven of Spades", "Two of Hearts", 1000)
    player3 = Player("1", "fold", "Seven of Spades", "Two of Hearts", 1500)
    print(player0 == player1)
    print(player0 == player2)
    print(player0 == player3)
    print(player0.firstcard == player3.firstcard)
    print(player0.state == player2.state)
    print(player0.state == player3.state)
    print(player0.chipsvalue == player2.chipsvalue)
    print(player0.chipsvalue == player3.chipsvalue)