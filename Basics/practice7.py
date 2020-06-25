import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self) #아이콘과 라벨 설정
        exitAction.setShortcut('Ctrl+Q') #단축키 설정
        exitAction.setStatusTip('Exit application') #상태바에 텍스트를 나타냄
        exitAction.triggered.connect(qApp.quit) #quit() 메서드를 클릭 시 생성되는 시그널과 연결되어 있다.

        self.statusBar()

        self.toolbar = self.addToolBar('Exit') #addToolBar를 이용하여 툴바를 만듦
        self.toolbar.addAction(exitAction) #addAction으로 툴바에 exitAction 동작을 추가함

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
