PlayerList = []
class Player:
	def __init__(self, position):
		self.position = position
		self.old = position
		PlayerList.append(self)
Player1 = Player(127)
