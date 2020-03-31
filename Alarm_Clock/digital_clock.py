import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt


class App(QWidget):

    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')

        # print(displayTxt)
        self.lbl.setText(displayTxt)

    def __init__(self):
        super().__init__()
        self.resize(250, 250)

        layout = QVBoxLayout()

        fnt = QFont('Open Sans', italic=True)
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(1000)


app = QApplication(sys.argv)

demo = App()
demo.show()

app.exit(app.exec_())
