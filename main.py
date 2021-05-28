import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

app = QApplication(sys.argv)
widget = QWidget()

textLabel = QLabel(widget)
textLabel.setText("Hello World!")
textLabel.move(110,85)

widget.setGeometry(50,50,320,200) #window.geometry('320x200+50+50')
widget.setWindowTitle("PyQt5 Example")	#window.title('Tk example')
widget.show()
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