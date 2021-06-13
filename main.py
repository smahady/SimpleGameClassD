
from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

class Character(Sprite):
	def __init__(self, thisScene, imageFile, xSize, ySize):
		super().__init__(thisScene, imageFile, xSize, ySize)


# sean mahady
class Sean(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/sean_sprite.png", 49, 55)
		self.x = 100	# 0 to 400
		self.y = 100
		self.dx = 1
		self.dy = -1
		self.boundAction = Scene.WRAP
	



# Animal
class IEATTERMITES(Character):
  def __init__(self,thisScene):
    super().__init__(thisScene, "sprites/niuniu_sprite.png",82,65)
    self.x = 125
    self.y = 180
    self.dx = 3
    self.dy = -10
    self.boundAction = Scene.WRAP
    
 

# 161x125
# Tian
class MEEEEEE(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/Tian_sprite.png" , 161, 125)
		self.x = 98
		self.y = 30
		self.dx = 3
		self.dy = -3
		self.boundAction = Scene.WRAP

# 112x173
#Jiayang
class SQUID(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/Jiayang_sprite.png", 112, 173)
		self.x = 150
		self.y = 150
		self.dx = 4
		self.dy = -4
		self.boundAction = Scene.WRAP



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		self.sean = Sean(self)
		self.SQUID = SQUID(self)
		self.MEEEEEE = MEEEEEE(self)
		self.IEATTERMITES = IEATTERMITES(self)
		

		
	def updateGame(self):
		print("My Update")
		self.spaceship.x +=1
		self.spaceship.update()
		self.sean.update()
		self.SQUID.update()
		self.IEATTERMITES.update()

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



# Sean Mahady's sprite
# https://opengameart.org/content/animated-turtle
# by Sogomn @ opengameart.org

# Jiayang's sprite
# 112x173
# https://opengameart.org/content/tnt-fun-sprite
# by Carlos Alface @ opengameart.org/

# Niuniu's sprite
# 82 x 65
# https://opengameart.org/content/cat-sprites
# by sheppardskin @ opengamerart.org/

# Tian's sprite
# 161x125
# https://opengameart.org/content/bird-and-explosion



# newton's sprite
# 28x32
#https://opengameart.org/content/2d-slime-animated