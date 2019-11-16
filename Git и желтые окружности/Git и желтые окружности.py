import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и желтые окружности.ui', self)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.drawf)
        self.show()

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        a = random.randint(40, 60)
        self.painter.drawEllipse(random.randint(0, 500), random.randint(0, 500), a,
                                 a)
        self.painter.end()

    def drawf(self):
        self.painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        a = random.randint(40, 60)
        self.painter.drawEllipse(random.randint(0, 500), random.randint(0, 500), a,
                                 a)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
