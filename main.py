from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		
	def updateGame(self):
		print("My Update")
		self.spaceship.x +=1
		self.spaceship.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())



from students import *

arr = []

arr.append(Doge())
arr.append(IEATTERMITES())
arr.append(Google())
arr.append(Animal())
arr.append(Glitch())
arr.append(ChaoticElephant())
arr.append(JUICYMONKYS())

for chara in arr:
	chara.move()