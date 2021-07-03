from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
from SimpleGame.Block import Block
from SimpleGame.Background import Background
import sys
from PyQt5.QtWidgets import QApplication
from enum import Enum

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing(Enum):
	RIGHT = 0
	LEFT = 1


app = QApplication(sys.argv)




class Ground(Block):
	def __init__(self, thisScene):
		spriteMaker = [["sprites/ground.png"] ] *30
		super().__init__(thisScene, spriteMaker, 120, 40)
		self.x = 0
		self.y = 500
		
	def update(self):
				
		super().update()

class Character(Sprite):
	def __init__(self, thisScene, sprite, x, y):
		self.state = States.FALLING
		self.facing = Facing.RIGHT
		super().__init__(thisScene, sprite, x, y)
		self.stateTimer = 0
		self.dy = 7 
		
	def update(self):
		if self.state == States.FALLING:
			if self.scene.ground.collidesWith(self):
				self.y = self.scene.ground.y - (self.height/2 + self.scene.ground.height / 2)
				self.standBehavior()
		elif self.state == States.STAND or self.state == States.WALK:
			if self.scene.keysDown[Scene.K_SPACE]:
				self.jumpBehavior()
			if self.scene.keysDown[Scene.K_RIGHT] or self.scene.keysDown[Scene.K_LEFT]:
				self.walkBehavior()
			if self.state == States.WALK:
				if (self.facing == facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] != True):
					self.standBehavior()
				if (self.facing == facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] != True):
					self.standBehavior()
		elif self.state == States.JUMP:
			self.stateTimer = self.stateTimer - 1
			print("Timer: ", self.stateTimer)
			if self.stateTimer < 1:
				self.dy = self.dy * -1
				self.state = States.FALLING
		super().update()

	def standBehavior(self):
		self.dy = 0
		self.dx = 0
		self.state = States.STAND
		self.pauseAnimation()

	# override this in your Character
	def jumpBehavior(self):
		pass

	# override this in your Character
	def walkBehavior(self):
		pass

# sean mahady
#250x100
# 50, 50
class Sean(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/sean_sheet.png", 250, 100)
		self.x = 75	
		self.y = 100
		self.dy = 1
		self.boundAction = Scene.WRAP
		self.loadAnimation(250, 100, 50, 50) 	# divides the sprite sheet into pieces
		self.generateAnimationCycles() 	#sets up each "cylce" into rows
		self.setAnimationSpeed(100)	#sets a QTimer to 100ms
		self.playAnimation()	#starts the QTimer

		#make a state for you class
		self.state = States.FALLING	#falling

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to 0, self.setCurrentCycle to 0, call the self.playAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and -10
	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 4
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.playAnimation()
			self.dx = -4

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	def jumpBehavior(self):
		self.stateTimer = 25
		self.dy = -4	
		self.state = States.JUMP

'''# newton's sprite
# 88x64
# 29x32
#Newton
class slimy(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/newton_sheet.png",88,64)
		self.x = 350
		self.y = 200
		self.dy = 3
		self.boundAction = Scene.WRAP
		self.loadAnimation(88, 64, 29, 32)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)
		self.playAnimation()
		self.state = 0
	def update(self):
		if self.y > 400:
			self.dy = 0
			self.y = 400
		super().update()'''
		

# Animal
#Sheet 480 x 240
# Cell: 80x60
class IEATTERMITES(Character):
  def __init__(self,thisScene):
    super().__init__(thisScene, "sprites/niuniu_sheet.png", 480, 240)
    self.x = 125
    self.y = 180
    self.dy = 10
    self.boundAction = Scene.WRAP

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		#loadAnimation(sheetX, sheetY, cellX, cellY)
    self.loadAnimation(480, 240, 80, 60)
    self.generateAnimationCycles()
    self.setAnimationSpeed(2147483647) #this is the highest number this will take
    self.playAnimation()  
  def update(self):
    super().update()

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and -10

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

# 112x173
# Jiayang
# Sheet: 484 x 346
# Cell: 96 x 173
class SQUID(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/jiayang_sheet.png", 484, 346)
		self.x = 150
		self.y = 150
		self.dx = 4
		self.dy = 4
		self.boundAction = Scene.WRAP

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		self.loadAnimation(484, 346, 96, 173)
		self.generateAnimationCycles()
		self.setAnimationSpeed(300)
		self.playAnimation()
	def update(self):
		super().update()

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and -10

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
    
    

    
 

# 400x144
# 100x72
# Tian
class MEEEEEE(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/tian_sheet.png" , 400, 144)
		self.x = 300
		self.y = 30
		self.dy = 4
		self.boundAction = Scene.WRAP
		self.loadAnimation(400, 144 , 100, 72)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)
		self.playAnimation()
		self.state = States.FALLING
	def update(self):
		super().update()

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and -10

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.





class Game(Scene):
	def __init__(self):
		super().__init__(600,600)

		super().__init__(600,600)
		self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)		


		self.ground = Ground(self)

		self.sean = Sean(self)
		self.SQUID = SQUID(self)
		self.MEEEEEE = MEEEEEE(self)
		self.IEATTERMITES = IEATTERMITES(self)
		# self.slimy = slimy(self)
		

		
	def updateGame(self):
		print("My Update")
		self.bg0.update()
		self.bg1.update()
		self.bg2.update()
		self.bg3.update()

		self.ground.update()

		self.sean.update()
		self.SQUID.update()
		self.IEATTERMITES.update()
		self.MEEEEEE.update()
		# self.slimy.update()

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