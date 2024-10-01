def solution(players, callings):
    player_rank = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        rank = player_rank[call]
        
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
        
        player_rank[players[rank]] = rank
        player_rank[players[rank - 1]] = rank - 1
    
    return players