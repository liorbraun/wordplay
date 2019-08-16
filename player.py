from wordgame import listofplayers

class add_player:
     def __init__(self, name, word="no word", opponent="no opponent"):
        self.name = name
        self.word = word
        self.opponent_name = opponent
        listofplayers.append(self)