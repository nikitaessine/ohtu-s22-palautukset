class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.points = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.same_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            
            return self.adventage_win()
        
        else:
            return f"{self.points[self.m_score1]}-{self.points[self.m_score2]}"


    def adventage_win(self):
        point_diff = self.m_score1 - self.m_score2

        if point_diff == 1:
            return f"Advantage {self.player1_name}"
        elif point_diff == -1:
            return f"Advantage {self.player2_name}"
        elif point_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"
    

    def same_score(self):
        if self.m_score1 < 4:
            return f"{self.points[self.m_score1]}-All"
        else:
            return "Deuce"
