import sys
from PyQt5 import QtGui, QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QLabel(w)
    b.setText("Hello World, I am Harshit! My first in PyQt5")
    w.setGeometry(200, 200, 500, 50)  # x,y,width, height
    b.move(50, 20)
    w.setWindowTitle("PyQt5 Prog_1")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
