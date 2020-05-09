from random import choice
from sys import (exit, argv)
from time import sleep
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSound
from PyQt5.QtGui import (QIcon, QPixmap, QFont)
from PyQt5.QtWidgets import (
    QToolTip, QPushButton, QApplication, QWidget, QLabel, QComboBox, QDesktopWidget)

# defining global variables

ICON = '../index.png'
DICE = ('one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png')
ROLLING_ANIMATION = 'animation.png'
SCALED_PARMS = 162, 302, Qt.KeepAspectRatio, Qt.FastTransformation
ONE_DICE_PARMS = 1427, 30, 162, 201
TWO_DICE_PARMS = 1265, 30, 324, 201
SLEEP_TIME = 0.5


class DiceRollSimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.die1 = QLabel(self)
        self.die1.setPixmap(QPixmap(choice(DICE)).scaled(*SCALED_PARMS))
        self.die1.move(0.5, 0.5)

        self.die2 = QLabel(self)
        self.die2.setPixmap(QPixmap(choice(DICE)).scaled(*SCALED_PARMS))
        self.die2.move(162, 0.5)
        self.die2.setVisible(False)

        self.btn = QPushButton('Roll It!', self)
        self.btn.setFont(QFont('SansSerif', 20))
        self.btn.setToolTip('Clicl to roll the die')
        self.btn.clicked.connect(self.rolldie)
        self.btn.resize(166, 43)
        self.btn.move(-2, 161)

        self.dice_amount = QComboBox(self)
        self.dice_amount.addItems(['1', '2'])
        self.dice_amount.activated[str].connect(self.dice_amount_changed)
        self.dice_amount.move(135, -2)

        QToolTip.setFont(QFont('SansSerif', 10))
        QApplication.desktop()
        screen = QDesktopWidget().screenGeometry()
        self.setFixedSize(162, 201)
        x = screen.width() - self.width() - 15
        self.move(x, 1)
        self.setWindowTitle('Dice Roll Simulator')
        self.setWindowIcon(QIcon(ICON))
        self.show()

    def rolldie(self):
        self.die1.setPixmap(QPixmap(ROLLING_ANIMATION).scaled(*SCALED_PARMS))
        self.die2.setPixmap(QPixmap(ROLLING_ANIMATION).scaled(*SCALED_PARMS))
        QApplication.processEvents()
        QSound.play("sound2.wav")
        sleep(SLEEP_TIME)

        self.die1.setPixmap(QPixmap(choice(DICE)).scaled(*SCALED_PARMS))
        self.die2.setPixmap(QPixmap(choice(DICE)).scaled(*SCALED_PARMS))
        QApplication.processEvents()

    def dice_amount_changed(self):
        geo = str(self.geometry())
        geo2 = geo[19:len(geo) - 1]
        loc = [int(x) for x in geo2.split(',')]

        if self.dice_amount.currentText() == '1':
            self.setFixedSize(162, 201)
            x = loc[0] + 154
            y = loc[1] - 30
            self.move(x, y)
            self.die2.setVisible(False)
            self.btn.resize(166, 43)
            self.dice_amount.move(132, -2)

        else:
            self.setFixedSize(324, 201)
            x = loc[0] - 170
            y = loc[1] - 30
            self.move(x, y)
            self.die2.setVisible(True)
            self.btn.resize(328, 43)
            self.dice_amount.move(294, -2)


if __name__ == '__main__':

    app = QApplication(argv)
    ex = DiceRollSimulator()
    ex.show()
    exit(app.exec_())
