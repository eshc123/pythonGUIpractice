import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) #툴팁 폰트 설정
        self.setToolTip('This is a <b>QWidget</b> widget') #setToolTip을 이용하여 표시될 텍스트 입력

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') #버튼에다 툴팁을 달아줌
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())