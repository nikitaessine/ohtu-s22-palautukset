class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):

        players = self.reader.get_players()
        sorted_players = []

        for player in players:
            if player.nationality == nationality:
                sorted_players.append(player)
        
        sorted_players = sorted(sorted_players, key=lambda x: x.assists + x.goals, reverse=True)

        return sorted_players        