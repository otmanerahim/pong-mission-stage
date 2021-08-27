class PlayerTournament:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def to_string(self):
        print("Point actuelle du joueur ", self.name, " : ", self.points)
