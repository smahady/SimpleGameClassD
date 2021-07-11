from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
from SimpleGame.Block import Block
from SimpleGame.Background import Background
import sys
from PyQt5.QtWidgets import QApplication
from enum import Enum
import random

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing():
	RIGHT = 0
	LEFT = 1


app = QApplication(sys.argv)

class Camera():
	def __init__(self, thisScene):
		self.viewWidth = Scene.width
		self.viewHeight = Scene.height
		self.scene = thisScene

	def follow(self, sprite):
		self.sprite = sprite

	def update(self):
		if self.sprite.drawX < 250:
			if self.sprite.x < 300:
				self.sprite.x = 300
			else:
				self.scene.offsetX -= 6
		if self.sprite.drawX > (350):
			if self.sprite.x > (26*120):
				self.sprite.x = (26*120)
			else:
				self.scene.offsetX += 6


class Ground(Block):
	def __init__(self, thisScene):
		spriteMaker = [["sprites/ground.png"] ] *30
		super().__init__(thisScene, spriteMaker, 120, 40)
		self.x = 0
		self.y = 500
		
	def update(self, offsetX, offsetY):
				
		super().update(offsetX, offsetY)

class Character(Sprite):
	def __init__(self, thisScene, sprite, x, y):
		self.state = States.FALLING
		self.facing = Facing.RIGHT
		super().__init__(thisScene, sprite, x, y)
		self.stateTimer = 0
		self.dy = 7 
		
	def update(self, offsetX, offsetY):
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
				if (self.facing == Facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] == None):
					self.standBehavior()
				if (self.facing == Facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] == None):
					self.standBehavior()
		elif self.state == States.JUMP:
			self.stateTimer = self.stateTimer - 1
			if self.stateTimer < 1:
				self.dy = self.dy * -1
				self.state = States.FALLING
		super().update(offsetX, offsetY)

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
		self.dy = 10
		self.boundAction = Scene.WRAP
		self.loadAnimation(250, 100, 50, 50) 	# divides the sprite sheet into pieces
		self.generateAnimationCycles() 	#sets up each "cylce" into rows
		self.setAnimationSpeed(10)	#sets a QTimer to 100ms
		self.playAnimation()	#starts the QTimer

		#make a state for you class
		self.state = States.FALLING	#falling

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to 0, self.setCurrentCycle to 0, call the self.playAnimation method. Set the DX to a value between 0 and 10. Set a State to States.WALK
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to 1, self.setCurrentCycle to 1, call the self.playAnimation method. Set the DX to a value between 0 and -10. Set a State to States.WALK
	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = 0
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 4
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = 1
			self.setCurrentCycle(1)
			self.playAnimation()
			self.dx = -4
			self.state = States.WALK

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	def jumpBehavior(self):
		self.stateTimer = 25
		self.dy = -4	
		self.state = States.JUMP

# newton's sprite
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
		self.state = States.FALLING
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)
		
	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = 0
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 7
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = 1
			self.setCurrentCycle(1)
			self.playAnimation()
			self.dx = -7
			self.state = States.WALK

	def jumpBehavior(self):
		self.stateTimer = 35
		self.dy = -7
		self.state = States.JUMP

# Animal
#Sheet 480 x 240
# Cell: 80x60
class IEATTERMITES(Character):
  def __init__(self,thisScene):
    super().__init__(thisScene, "sprites/niuniu_sheet.png", 480, 240)
    self.x = 125
    self.y = 180
    self.dy = 10

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		#loadAnimation(sheetX, sheetY, cellX, cellY)
    self.loadAnimation(480, 240, 80, 60)
    self.generateAnimationCycles()
    self.setAnimationSpeed(30) #this is the highest number this will take
    self.playAnimation()  
  def update(self, offsetX, offsetY):
    super().update(offsetX, offsetY)


  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
      self.facing = 0
      self.setCurrentCycle(Facing.RIGHT)
      self.playAnimation()
      self.dx = 15
      self.state = States.WALK
    elif self.scene.keysDown[Scene.K_LEFT]:
      self.facing = 1
      self.setCurrentCycle(2)
      self.playAnimation()
      self.dx = -15
      self.state = States.WALK

  def jumpBehavior(self):
    self.stateTimer = 30
    self.dy = -10
    self.state = States.JUMP		

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
		self.setAnimationSpeed(30)
		self.playAnimation()
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)


	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.playAnimation()
			self.dx = 10
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.playAnimation()
			self.dx = -10
			self.state = States.WALK
	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	def jumpBehavior(self):
		self.dy = -10
		self.stateTimer = 33
		self.state = States.JUMP



    
 

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
		self.setAnimationSpeed(30)
		self.playAnimation()
		self.state = States.FALLING
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)

	def walkBehavior(self):
		if self.scene.keysDown[Scene.K_RIGHT]:
			self.facing = 0
			self.setCurrentCycle(0)
			self.playAnimation()
			self.dx = 15
			self.state = States.WALK
		elif self.scene.keysDown[Scene.K_LEFT]:
			self.facing = 1
			self.setCurrentCycle(1)
			self.playAnimation()
			self.dx = -15
			self.state = States.WALK
			
	def jumpBehavior(self):
		self.stateTimer = 26
		self.dy = -6	
		self.state = States.JUMP





class Spaceship(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/spaceship100.png", 100, 100)
		self.x = 300
		self.y = 100
		self.dx = 6
		self.timer = 60
		self.enemies = []
	def checkBounds(self):

		if self.drawX < 0:
			self.dx = 6
		if self.drawX > 550:
			self.dx = -6
		self.timer -= 1
		if self.timer < 1:
			self.timer = 60
			self.enemySpawn()

		for enemy in self.enemies:
			enemy.update(self.scene.offsetX, self.scene.offsetY)

	def enemySpawn(self):
		temp = random.randint(0,2)
		newEnemy = 0
		if temp == 0:
			newEnemy = Enemy(self.scene, self.x, self.y)
		elif temp==1:
			newEnemy = GroundEnemy(self.scene, self.x, self.y)
		elif temp ==2:
			newEnemy = FlyingEnemy(self.scene, self.x, self.y)
		self.enemies.append(newEnemy)

# Abstract base class
class BaseEnemy(Sprite):
	def __init__(self, thisScene, file, width, height, x, y):
		super().__init__(thisScene, file, width, height)
		self.setBoundAction(Scene.DIE) #WRAP, BOUNCE, CONTINUE, DIE, STOP
		self.x = x
		self.y = y
		self.dy = 3
		self.timer = 30	#determines how often the enemy makes a choice
	def update(self, offsetX, offsetY):
		self.timer -= 1
		if self.timer < 1:
			self.makeDecision()
		super().update(offsetX, offsetY)
	def makeDecision(self):
		pass

class Enemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/egg3.png", 128, 128, x, y)
	def update(self, offsetX, offsetY):
		super().ypdate(offsetX, offsetY)
	def makeDecision(self):
		self.dy = 3

class GroundEnemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/egg3.png", 128, 128, x, y)
	def update(self, offsetX, offsetY):
		super().ypdate(offsetX, offsetY)
	def makeDecision(self):
		self.dy = 3

class FlyingEnemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/egg3.png", 128, 128, x, y)
	def update(self, offsetX, offsetY):
		super().ypdate(offsetX, offsetY)
	def makeDecision(self):
		self.dy = 3




		


class Game(Scene):
	def __init__(self):
		super().__init__(600,600)

		self.camera = Camera(self)

		self.changeBoundSize((25*120), 600)

		self.offsetX = 20
		self.offsetY = 20
		
		self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)		


		self.ground = Ground(self)

		self.main = Sean(self)
		self.SQUID = SQUID(self)
		self.MEEEEEE = MEEEEEE(self)
		self.IEATTERMITES = IEATTERMITES(self)
		self.slimy = slimy(self)

		self.spaceship = Spaceship(self)

		self.camera.follow(self.main)
		

		
	def updateGame(self):
		
		self.bg0.update(self.offsetX, self.offsetY)
		self.bg1.update(self.offsetX, self.offsetY)
		self.bg2.update(self.offsetX, self.offsetY)
		self.bg3.update(self.offsetX, self.offsetY)

		self.ground.update(self.offsetX, self.offsetY)

		self.main.update(self.offsetX, self.offsetY)
		self.SQUID.update(self.offsetX, self.offsetY)
		self.IEATTERMITES.update(self.offsetX, self.offsetY)
		self.MEEEEEE.update(self.offsetX, self.offsetY)
		self.slimy.update(self.offsetX, self.offsetY)

		self.spaceship.update(self.offsetX, self.offsetY)

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