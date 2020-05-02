''' class responsible for round managing'''

import ruler
import utils
from player import Player

class Round:
    def __init__(self, round_turn, flop_cards = [], turn_cards = [], river_cards = []):
        self.round_turn = round_turn
        self.flop_cards = flop_cards
        self.turn_cards = turn_cards
        self.river_cards = river_cards

def deal_cards_table(round_turn, players, ruler, flop_cards, turn_cards, river_cards): #function deals flop, turn, and river (!no burnt cards between deal!)
    if round_turn == 1: #condition on beginning of turn after conditions on dealing the flop met
        for i in range(3):
            flop_cards.append(ruler.pop()) #build flop for the round
        for player in players:
            if player.state != 'fold':
                player.state = 'flop'  #for all player not folded, update state to flop (reached the flop)
    if round_turn == 2: #condition on beginning of turn after conditions on dealing the turn met
        turn_cards.append(ruler.pop())
        for player in players:
            if player.state != 'fold':
                player.state = 'turn'
    if round_turn == 3: #condition on beginning of turn after conditions on dealing the river met
        river_cards.append(ruler.pop())
        for player in players:
            if player.state != 'fold':
                player.state = 'river'

def best_player_hand(players): #function determines winner around the table
    for player in players:
        if player.state != 'fold':
            player.hand = player.first_card + player.second_card + poker_round.flop_cards + poker_round.turn_cards + poker_round.river_cards
            # build highest hand possible
            player.hand = utils.find_best(player.hand)
            player.hand_name = 'High Card'

            if utils.find_pairs(player) != []:
                high_card = utils.find_best(player.hand) #descending high card
                player.hand = utils.find_pairs(player.hand)
                if len(player.hand) >= 4 :
                    for index in range(len(player.hand)-4): #reduce hand to 4 cards if len above 4
                        player.hand.pop()
                    player.hand_name = 'Two Pairs'
                else:
                    player.hand_name = 'One Pair'
                for high in high_card:
                    if (not(high in player.hand) and len(player.hand)<5): #build up to 5 with highest card afeter pairs
                        player.hand.append(high)
                        

            if utils.find_triplet(player.hand) != [] : #building three of a kind
                high_card = utils.find_best(player.hand) #descending high card
                player.hand = utils.find_triplet(player.hand)
                if len(player.hand) > 3 :
                    for index in range(len(player.hand)-3): #reduce hand to 3 cards if len above 3
                        player.hand.pop()
                for high in high_card:
                    if (not(high in player.hand) and len(player.hand)<5): #build up to 5 with highest card afeter pairs
                        player.hand.append(high)
                player.hand_name = 'Three of a kind'

            if utils.find_straight(player.hand) != []: #condition on straight
                    player.hand = utils.find_straight(player.hand) #straight
                    player.hand_name = 'Straight'
            
            if utils.find_color != []:
                player.hand = utils.find_color(player.hand)
                player.hand_name = 'Flush'
            
            if utils.find_triplet(player.hand) != [] : #building fullhouse
                if utils.find_pairs(player.hand) != []:
                    player.hand = utils.find_triplet(player.hand) + utils.find_pairs(player.hand)
                elif len(utils.find_triplet(player.hand)) == 6:
                    player.hand = utils.find_triplet(player.hand)
                    player.hand.pop()
                player.hand_name = 'Ful House'
                
            if utils.find_four(player.hand) != []: #conditions on not empty
                player.hand = utils.find_four(player.hand) #probable syntax error
                for high in high_card:
                    if (not(high in player.hand) and len(player.hand)<5): #build up to 5 with highest card afeter four of a kind
                        player.hand.append(high)
                player.hand_name = 'Four of a kind'


            if utils.find_color(player.hand) != []: #condition on color
                player.hand = utils.find_color(player.hand) #color
                if utils.find_straight(player.hand) != []: #condition on straight in color
                    player.hand = utils.find_straight(player.hand) #straight flush
                    if player.hand[0] == 13:
                        player.hand_name = 'Royal Flush'
                    else:
                        player.hand_name = 'Straight Flush'



            
            
            


def give_pot_to_round_winner(winner): # function gives pot to winner !corner cases to deal with!
    print()

ruler = ruler.Ruler()
print(ruler.deck)
poker_round = Round(1)
player0 = Player(0, 120, 'call', 30, '', '', 200)
player1 = Player(1, 120, 'allin', 30, '', '', 200)
deal_cards_table(1, [player0, player1], ruler.deck, poker_round.flop_cards, poker_round.turn_cards, poker_round.river_cards)
give_pot_to_round_winner(player0)
print(player0.state)
print(player0.chips_value)
print(player1.state)
print(player1.chips_value)