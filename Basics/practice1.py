#파이썬 GUI 실습 프로젝트

import sys
from PyQt5.QtWidgets import QApplication, QWidget #QtWidgets에는 기본적인 UI를 제공하는 위젯이 있다.


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300) #위젯을 화면 좌표 위치로 이동
        self.resize(400, 200) #위젯의 사이즈를 조정
        self.show() #위젯을 보여줌


if __name__ == '__main__': #__name__은 현재 모듈의 이름이 저장되는 내장 변수임 import 하면 이 파이썬 파일의 이름이 __name__이 됨.
                           # 직접 실행시키면 __name__은 __main__이 됨. 이 코드를 통해 직접 실행되는지 모듈로 실행되는지 알 수 있음.
   app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야한다.
   ex = MyApp()
   sys.exit(app.exec_())