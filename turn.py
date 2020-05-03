import ruler

def get_player_state(player):
    return(player.state)

def find_last_not_folded(players): #return the last player not folded if last one around the table | function called after each player's turn
    states = list(map(get_player_state, players))
    if states.count('fold') == (len(players)-1):
        for player in players:
            if player.state != 'fold':
                return(player)