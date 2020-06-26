import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry() #frameGeometry 는 창의 위치, 크기 정보를 가져온다.
        cp = QDesktopWidget().availableGeometry().center() #사용하는 모니터의 화면 중앙 위치 정보를 가져온다.
        qr.moveCenter(cp) #qr 창의 직사각형 중심을 모니터의 화면 중앙 정보인 cp로 이동?함
        self.move(qr.topLeft()) #self 현재 창을 화면의 중심으로 이동한 qr의 위치로 이동하게 됨


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())