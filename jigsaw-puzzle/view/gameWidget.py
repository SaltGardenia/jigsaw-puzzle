from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
import random
# 游戏页面
class gameWidget(QWidget):
    signalGame2Log = pyqtSignal()
    def __init__(self, width = 1100, height = 950):
        super().__init__()
        self.width = width
        self.height = height
        self.setWindowTitle('拼图游戏')
        self.setWindowIcon(QIcon('img/icon.png'))
        self.setFixedSize(self.width, self.height)

        # 载入初始图片
        self.lLayout = QGridLayout()
        self.labs = []
        for i in range(3):
            for j in range(3):
                lab = QLabel()
                lab.setPixmap(QPixmap('img/{}.png'.format(3*i+j+1)))
                self.labs.append(lab)
                self.lLayout.addWidget(lab, i, j)

        # 初始化控件
        self.startBtn = QPushButton('开始游戏', self)
        self.changeBtn = QPushButton('移形换影', self)  # 右侧按钮
        self.resetBtn = QPushButton('重新开始', self)
        self.helpBtn = QPushButton('帮助', self)
        self.retBtn = QPushButton('返回', self)

        self.startBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.changeBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.resetBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.helpBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.retBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')

        self.startBtn.clicked.connect(self.randomImg)
        self.resetBtn.clicked.connect(self.randomImg)
        self.retBtn.clicked.connect(self.fGame2Log)
        self.resetBtn.hide()
        self.changeBtn.hide()

        # 计数器
        self.num = 0
        self.numLable = QLabel('操作次数:{}'.format(self.num), self)
        self.numLable.setStyleSheet('color:black; font-size:22px; font-weight:bold')
        self.numLable.hide()

        # Layout
        self.rLayout = QVBoxLayout() # 创建右侧垂直管理器
        self.rLayout.addWidget(self.startBtn)
        self.rLayout.addWidget(self.changeBtn)
        self.rLayout.addWidget(self.resetBtn)
        self.rLayout.addWidget(self.helpBtn)
        self.rLayout.addWidget(self.retBtn)
        self.rLayout.addStretch()   # 下至弹簧
        self.rLayout.addWidget(self.numLable)
        self.rLayout.addStretch()
        self.rLayout.setContentsMargins(10, 10, 10, 10)

        self.totalLayout = QHBoxLayout()
        self.totalLayout.addLayout(self.lLayout)
        self.totalLayout.addLayout(self.rLayout)
        self.setLayout(self.totalLayout)

    # 随机图片
    def randomImg(self):
        self.resetBtn.show()
        self.startBtn.hide()
        self.numLable.show()
        for lab in self.labs:
            self.lLayout.removeWidget(lab)
            lab.hide()
        self.random_list = random.sample(list(range(1, 10)), 9)
        self.x = random.randint(0, 2)
        self.y = random.randint(0, 2)
        for i in range(3):
            for j in range(3):
                lab = QLabel()
                lab.setPixmap(QPixmap('img/{}.png'.format(self.random_list[3*i+j])))
                self.labs.append(lab)
                if self.x == i and self.y == j:
                    continue
                self.lLayout.addWidget(lab, i, j)
                lab.show()


    # 交换图片
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            x = QMouseEvent.x()
            y = QMouseEvent.y()
            i = (y-20) // 300
            j = (x-20) // 300
            if i == self.x-1 and j == self.y or i == self.x+1 and j == self.y or i == self.x and j == self.y-1 or i == self.x and j == self.y+1:
                tmp = self.random_list[3 * self.x + self.y]
                self.random_list[3*self.x + self.y] = self.random_list[3*i+j]
                self.random_list[3 * i + j] = tmp
                self.x = i
                self.y = j
                for lab in self.labs:
                    self.lLayout.removeWidget(lab)
                    lab.hide()
                for i in range(3):
                    for j in range(3):
                        lab = QLabel()
                        lab.setPixmap(QPixmap('img/{}.png'.format(self.random_list[3*i+j])))
                        self.labs.append(lab)
                        if self.x == i and self.y == j:
                            continue
                        self.lLayout.addWidget(lab, i, j)
                        lab.show()
                self.num += 1
                self.numLable.setText('操作次数:{}'.format(self.num))
                if self.random_list == list(range(1, 10)):
                    QMessageBox.information(self, '游戏提示', '你赢了')


    # 游戏返回登录槽函数
    def fGame2Log(self):
        self.signalGame2Log.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = gameWidget()
    test.show()
    sys.exit(app.exec())