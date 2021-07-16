# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('MyProject')
        self.setWindowIcon(QIcon('Assets/web.png'))
        self.setGeometry(500, 500, 300, 200)
        self.show()

# __name__은 현재 모듈 이름이 저장되는 내장 변수
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())

