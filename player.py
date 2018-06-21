PlayerList = []
class Player:
	def __init__(self, position, ID):
		self.position = position
		self.old = position + 1
		self.id = ID
		PlayerList.append(self)
Player1 = Player(0, 1)
