import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self) #버튼을 만드는데 첫 파라미터는 버튼에 표시될 텍스트, 두 번째는 버튼이 위치할 부모 위젯
      btn.move(0, 0)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit) #버튼의 clicked와 인스턴스의 quit 메서드에 연결됨
        #qCoreApplication.instance()는 어플리케이션 객체?를 나타내므로 객체의 종료와 버튼의 클릭을 연결해준다는 말

      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())