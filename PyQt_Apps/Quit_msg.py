import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('index.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = 0
d = dict()

for line in handle:

     if not line.startswith("From"):
         continue
        line = line.split()
        if line[0] =='From':
            name = line[1]

             for word in name.split():
                 d[word] = d.get(word, 0)+1
             count += 1
maximum = None
k = None
for key, value in d.items():
    if maximum is N one or value >maximum:
        maximum = value
        k = key
print(k, maximum)
