import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# 验证码
class myCode(QLabel):
    def __init__(self, parent=None, w = 100, h = 50):
        super().__init__()
        self.w = w
        self.h = h
        self.__text = ''

        self.pixmap = QPixmap(self.w, self.h)
        self.painter = QPainter(self.pixmap)
        self.painter.setBrush(QBrush(QColor('#bbb')))
        self.painter.drawRect(0, 0, self.w, self.h)
        self.code = self.draw_text()
        self.setPixmap(self.pixmap)


    def draw_text(self):
        self.__text = ''
        str = 'abcdefghijklmnopqrstuvwxyz1234567890'
        for i in range(4):
            index = random.randint(0, len(str) - 1)
            ch = str[index]
            self. __text += ch
        self.painter.setFont(QFont('宋体', 16))
        for i in range(4):
            self.painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.painter.drawText(int(i*self.w/4+10), self.h-10, self.__text[i])

    def mousePressEvent(self, QMouseEvent):
        self.painter.drawRect(0, 0, self.w, self.h)
        self.draw_text()
        self.setPixmap(self.pixmap)

    def updateCode(self):
        self.painter.drawRect(0, 0, self.w, self.h)
        self.draw_text()
        self.setPixmap(self.pixmap)

    @property
    def text(self):
        return self.__text