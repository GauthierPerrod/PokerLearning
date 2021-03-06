''' Class responsible for the actions of a player.
A player has an absolute position around the table, a starting hand composed of 2 dealt cards, a given value of chips, 
and a number of states possible, e.g: dealt, flop, turn, river, call, bet, raise, fold, allin'''

class Player:
    def __init__(self, character, absolute_position, time_bank, state, timer, first_card, second_card, chips_value, hand=None):
        self.character = character #either 'human' or 'computer'
        self.absolute_position = absolute_position
        self.time_bank = time_bank
        self.state = state
        self.timer = timer
        self.first_card = first_card
        self.second_card = second_card
        self.chips_value = chips_value
        self.hand = hand
        self.hand_name = None
        self.player_pot = None
        self.is_folded = None
        
    #Method to print the dealt hand of the player
    def __str__(self):
        return('position : ' + str(self.absolute_position) + " & " + "time bank : " + str(self.time_bank) + "\n"
        'state : ' + str(self.state) + ' & ' + 'timer : ' + str(self.timer) + "\n"
        'dealt hand : ' + str(self.first_card) + " & "+ str(self.second_card) + "\n"
        'chips value : ' + str(self.chips_value))
    def __repr__(self):
        return('Position around the table : ' + str(self.absolute_position) + " & " + "Time Bank : " + str(self.time_bank) + "\n"
        'State : ' + str(self.state) + ' & ' + 'Timer : ' + str(self.timer) + "\n"
        'Dealt Hand : ' + str(self.first_card) + ' & ' + str(self.second_card) +"\n"
        'Chips Value : ' + str(self.chips_value))
    #Override
    def __eq__(self, other):
        return(self.__dict__ == other.__dict__)
    
    def play_turn(self, game_state):
        player_action = {}
        if not self.is_folded :
            if self.character == 'human' :

                action =""
                while action not in ['fold', 'check', 'call', 'bet'] :
                    print('Please enter <Fold, Check, Call or  Bet>')
                    action = input().lower()
                player_action['action']=action

                if action=='bet' :
                    bet_chips = 0.0
                    while not  game_state['big_blind'] + game_state['current_bet'] <= float(bet_chips):
                        print('Enter a value bigger than the current bet plus one big blind')
                        bet_chips = float(input())
                    if bet_chips > self.player_pot :
                        bet_chips = self.player_pot
                    player_action['bet'] = bet_chips
        return(player_action)



if __name__ == "__main__":
    player0 = Player('human', "0", 120, "dealt", 30, "Seven of Spades", "Two of Hearts", 1000)
    print(player0)
    player1 = Player('human', "1", 120, "dealt", 30, "Jack of Spades", "Ten of Clubs", 1000)
    player2 = Player('human', "0", 120, "dealt", 30, "Seven of Spades", "Two of Hearts", 1000)
    player3 = Player('human', "1", 120, "fold", 30, "Seven of Spades", "Two of Hearts", 1500)
    print(player0 == player1)
    print(player0 == player2)
    print(player0 == player3)
    print(player0.first_card == player3.first_card)
    print(player0.state == player2.state)
    print(player0.state == player3.state)
    print(player0.chips_value == player2.chips_value)
    print(player0.chips_value == player3.chips_value)