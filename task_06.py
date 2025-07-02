class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):

    if len(players) != 2:
        raise WrongNumberOfPlayersError
    
    if (players[0][1] in ['R', 'S', 'P']) == False or (players[1][1] in ['R', 'S', 'P']) == False:
        raise NoSuchStrategyError
        
    move1 = players[0][1]
    move2 = players[1][1]
    
    
    if move1 == move2:
        return f"{players[0][0]} {move1}"
    
    
    rules = {'R': 'S', 'S': 'P', 'P': 'R'}
    
    
    if rules[move1] == move2:
        return f"{players[0][0]} {move1}"
    else:
        return f"{players[1][0]} {move2}"
    
    
        
    return print(0)   
        
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))


#Done


    