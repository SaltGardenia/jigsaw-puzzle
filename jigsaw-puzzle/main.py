import sys
from view.gameWidget import *
from view.loginWidget import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
class game():
    def __init__(self):
        self.login = loginWidget()
        self.game = gameWidget()
        self.game.signalGame2Log.connect(self.fGame2Log)

    # 主线逻辑
    def main(self):
        self.login.show()
        self.login.signalLog2Game.connect(self.fGameStart)  # 登录成功信号连接

    # 登录成功槽函数
    def fGameStart(self):
        self.game.show()
        self.login.close()

    # 游戏返回登录槽函数
    def fGame2Log(self):
        self.login.show()
        self.game.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = game()
    game.main()
    sys.exit(app.exec())