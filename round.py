''' class responsible for round managing'''

import ruler
import utils
from player import Player

class Round:
    def __init__(self, round_turn, flop_cards = [], turn_cards = [], river_cards = []):
        self.hand_ranking = {'Royal Flush':10, 'Straight Flush':9, 'Four of a kind':8, 'Full House':7, 'Flush':6, 'Straight':5, 'Three of a kind':4, 'Two Pairs':3, 'One Pair':2, 'High Card':1}
        self.round_turn = round_turn
        self.flop_cards = flop_cards
        self.turn_cards = turn_cards
        self.river_cards = river_cards

def deal_cards_player(players, ruler):
    for index in range(2):
        for player in players:
            if index == 0:
                player.first_card = ruler.pop()
            if index == 1:
                player.second_card = ruler.pop()

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
            player.hand = [player.first_card, player.second_card]
            for card in poker_round.flop_cards:
                player.hand.append(card)
            for card in poker_round.turn_cards:
                player.hand.append(card)
            for card in poker_round.river_cards:
                player.hand.append(card)
            print(player.hand)
            # build highest hand possible
            player_new_hand = utils.find_best(player.hand)
            player.hand_name = 'High Card'

            if len(utils.find_pairs(player.hand)) != 0:
                high_card = utils.find_best(player.hand) #descending high card
                player_new_hand = utils.find_pairs(player.hand)
                if len(player_new_hand) >= 4 :
                    for index in range(len(player_new_hand)-4): #reduce hand to 4 cards if len above 4
                        player_new_hand.pop()
                    player.hand_name = 'Two Pairs'
                else:
                    player.hand_name = 'One Pair'
                for high in high_card:
                    if (not(high in player_new_hand) and len(player_new_hand)<5): #build up to 5 with highest card afeter pairs
                        player_new_hand.append(high)
                        

            if len(utils.find_triplet(player.hand)) != 0 : #building three of a kind
                high_card = utils.find_best(player.hand) #descending high card
                player_new_hand = utils.find_triplet(player.hand)
                if len(player_new_hand) > 3 :
                    for index in range(len(player_new_hand)-3): #reduce hand to 3 cards if len above 3
                        player_new_hand.pop()
                for high in high_card:
                    if (not(high in player_new_hand) and len(player_new_hand)<5): #build up to 5 with highest card afeter pairs
                        player_new_hand.append(high)
                player.hand_name = 'Three of a kind'

            if len(utils.find_straight(player.hand)) != 0: #condition on straight
                    player_new_hand = utils.find_straight(player.hand) #straight
                    player.hand_name = 'Straight'
            
            if len(utils.find_color(player.hand)) != 0:
                player_new_hand = utils.find_color(player.hand)
                player.hand_name = 'Flush'
            
            if len(utils.find_triplet(player.hand)) != 0 : #building fullhouse
                if len(utils.find_pairs(player.hand)) != 0:
                    player_new_hand = utils.find_triplet(player.hand) + utils.find_pairs(player.hand)
                    player.hand_name = 'Full House'
                elif len(utils.find_triplet(player.hand)) == 6:
                    player_new_hand = utils.find_triplet(player.hand)
                    player_new_hand.pop()
                    player.hand_name = 'Full House'
                
            if len(utils.find_four(player.hand)) != 0: #conditions on not empty
                player_new_hand = utils.find_four(player.hand) #probable syntax error
                for high in high_card:
                    if (not(high in player_new_hand) and len(player_new_hand)<5): #build up to 5 with highest card afeter four of a kind
                        player_new_hand.append(high)
                player.hand_name = 'Four of a kind'


            if len(utils.find_color(player.hand)) != 0: #condition on color
                player_flush = utils.find_color(player.hand) #color
                if len(utils.find_straight_flush(player_flush)) != 0: #condition on straight in color
                    player_new_hand = utils.find_straight_flush(player_flush) #straight flush
                    if player.hand[0] == 13:
                        player.hand_name = 'Royal Flush'
                    else:
                        player.hand_name = 'Straight Flush'

            player.hand = player_new_hand #update player's hand too best hand found (list of objects card to list of hand value)
            print(player.hand)

def find_winner_after_river(players): #find the winner among players not folded after the river
    among_players = list(players)
    best_hand = [among_players.pop()] #set player as reference for comparison with others in hand ranking

    for player in among_players: #build player list with best hand_name
        if player.state != 'fold':
            if poker_round.hand_ranking[player.hand_name] > poker_round.hand_ranking[best_hand[0].hand_name]:
                best_hand = []
                best_hand.append(player)
            elif poker_round.hand_ranking[player.hand_name] == poker_round.hand_ranking[best_hand[0].hand_name]:
                best_hand.append(player)

    if len(best_hand)>1: #if more than one player with best hand_name distinguish best hand if it exists
        winner = [best_hand.pop()] #set a player as winner to compare other players with
        for player in best_hand:
            player_hand = player.hand # extract player hand to compare with winner's hand
            if ((winner[0].hand_name != 'Straight') and (winner[0].hand_name != 'Straight Flush') and (winner[0].hand_name != 'Royal Flush')): #if hand different from a straight (len(player_hand) at least 5 items)
                for index in range(5):
                    if player_hand[index] > winner[0].hand[index]: #if player's hand better than winner, new winner is player, stop comparison
                        winner = [player]
                        break
                    elif player_hand[index] < winner[0].hand[index]: #if player's hand is worse at some point, stop comparison with this player
                        break
                    elif ((player_hand[index] == winner[0].hand[index]) and (index == 4)): #if player's hand isn't better or worse and loop reached end of hand, both player have same hand, append player to winner list
                        winner.append(player)
            else:
                if player_hand[0] > winner[0].hand[0]:
                    winner = [player]
                elif player_hand[0] == winner[0].hand[0]:
                    winner.append(player)
        return(winner)

    else:
        return(best_hand)

    
def give_pot_to_round_winner(winner, players): # function gives pot to winner !corner cases to deal with!
    winner_sorted = sorted(winner, key = lambda x: x.player_pot) #sort winner list by ascending player_pot

    for index in range(len(winner_sorted)):
        for player in players:
            if not(player in winner_sorted): #for each player not winner, check player_pot and distribute contribution to winner
                if (player.player_pot / (len(winner_sorted) - index)) > (winner_sorted[index].player_pot):
                    winner_sorted[index].chips_value += winner_sorted[index].player_pot
                    player.player_pot -= winner_sorted[index].player_pot
                else:
                    winner_sorted[index].chips_value += (player.player_pot // (len(winner_sorted) - index))
                    player.player_pot -= (player.player_pot // (len(winner_sorted) - index))
        winner_sorted[index].chips_value += winner_sorted[index].player_pot #claim own player_pot when winner
        winner_sorted[index].player_pot = 0

def settle_remaining_pot(winner,players): #settle remaining pot by finding next winner until all pot distributed
    remaining_players = list(players)
    for player in players: #do it for all players, to make sure to distribute all remaining player_pot
        if player.state != 'fold':
            for player1 in players:
                if player1.player_pot > 0: #if player still active after river and player_pot > 0, remove previous winner and find new winner and distribute remaining_pot
                    for win in winner:
                        remaining_players.remove(win)
                    winner = find_winner_after_river(remaining_players)
                    print(winner)
                    give_pot_to_round_winner(winner, remaining_players)

        


if __name__ == '__main__':
    #create ruler
    ruler = ruler.Ruler()
    print(ruler.deck)

    #create player
    player0 = Player('human', 0, 120, 'check', 30, '', '', 200)
    player1 = Player('human', 1, 120, 'check', 30, '', '', 200)
    player2 = Player('human', 2, 120, 'check', 30, '', '', 200)
    player0.player_pot = 30
    player1.player_pot = 45
    player2.player_pot = 40

    #create players
    players = [player0, player1, player2]

    #create round
    poker_round = Round(0)

    #deal cards
    deal_cards_player(players, ruler.deck)

    #deal_cards_table
    poker_round.round_turn = 1
    deal_cards_table(poker_round.round_turn, players, ruler.deck, poker_round.flop_cards, poker_round.turn_cards, poker_round.river_cards)
    poker_round.round_turn = 2
    deal_cards_table(poker_round.round_turn, players, ruler.deck, poker_round.flop_cards, poker_round.turn_cards, poker_round.river_cards)
    poker_round.round_turn = 3
    deal_cards_table(poker_round.round_turn, players, ruler.deck, poker_round.flop_cards, poker_round.turn_cards, poker_round.river_cards)

    #best_player_hand
    best_player_hand(players)

    #find_winner_after_river
    print(find_winner_after_river(players)[0].hand_name)
    print(find_winner_after_river(players))
    winner = find_winner_after_river(players)

    #give_pot_to_round_winner
    give_pot_to_round_winner(winner, players)

    #settle_remaining_pot
    settle_remaining_pot(winner, players)

    print(player0.chips_value)
    print(player1.chips_value)
    print(player2.chips_value)
