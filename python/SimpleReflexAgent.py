import L3_cleaner_SSD
'''
A simple memory-less deterministic reflex agent

if-then rules
If dirty then suck up dirt
If not facing wall and clean then go forward
If facing wall and clean then turn right
If facing wall and at home then turn off
'''
class SimpleReflexAgent(L3_cleaner_SSD.Cleaner):
	def __init__(self, probTurnLeft, probTurnRight,probTurnOff,probMove):
		L3_cleaner_SSD.Cleaner.__init__(self)
		random.seed()
		self.probTurnLeft = probTurnLeft
		self.probTurnRight = probTurnRight
		self.probTurnOff = probTurnOff
		self.probMove = probMove
	def Agent(self, grid):
		 isFacingWall = self.SenseWall(grid)
		 isDirty      = self.SenseDirt(grid)
		 isHome       = self.SenseHome()

		 if isDirty:
		 	return self.ActSuckDirt
		 else:
		 	if isFacingWall:
		 		if isHome:
		 			return self.ActTurnOff
		 		else:
		 			return self.ActTurnRight
		 	else:
		 		return self.ActMove
