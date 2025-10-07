from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from view.regWidget import regWidget
from data.tool import *
from view.myCode import *
# 登录页
class loginWidget(QWidget):
    signalLog2Game = pyqtSignal()   # 登录成功信号
    def __init__(self, width = 1000, height = 600):
        super().__init__()
        self.width = width
        self.height = height
        self.userData = data()  # 初始化用户列表
        self.reg = regWidget(self.userData)
        self.reg.signalReg2Log.connect(self.fReg2Log)    # 注册返回登录信号

        self.setWindowTitle('登录窗口')
        self.resize(self.width, self.height)    # 设置窗口大小
        self.setWindowIcon(QIcon('img/icon.png'))   # 设置窗口图标

        win_palette = QPalette()
        win_palette.setBrush(self.backgroundRole(), QBrush(QPixmap('img/bgd.jpg').scaled(self.size())))
        self.setPalette(win_palette)


        # Lable
        self.nameLable = QLabel('用户名', self)
        self.pwdLable = QLabel(' 密码 ', self)
        self.captchaLable = QLabel('验证码', self)
        self.codeLable = myCode(self)

        self.nameLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')
        self.pwdLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')
        self.captchaLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')

        # Edit
        self.nameEdit = QLineEdit('', self)
        self.pwdEdit = QLineEdit('', self)
        self.captchaEdit = QLineEdit('', self)

        self.nameEdit.setPlaceholderText('请输入6-10位用户名')
        self.pwdEdit.setPlaceholderText('请输入密码')
        self.captchaEdit.setPlaceholderText('请输入验证码')

        self.nameEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')
        self.pwdEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')
        self.captchaEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')

        self.captchaEdit.setMaxLength(4)

        self.nameEdit.installEventFilter(self)  # 事件监听
        self.pwdEdit.installEventFilter(self)
        self.captchaEdit.installEventFilter(self)

        # Tips
        self.nameTips = QLabel('', self)    # 提示
        self.pwdTips = QLabel('', self)
        self.captchaTips = QLabel('', self)

        self.nameTips.setStyleSheet('color:red; font-size:22px; font-weight:bold')
        self.pwdTips.setStyleSheet('color:red; font-size:22px; font-weight:bold')
        self.captchaTips.setStyleSheet('color:red; font-size:22px; font-weight:bold')

        # Layout
        self.nameLine = QHBoxLayout()
        self.pwdLine = QHBoxLayout()
        self.captchaLine = QHBoxLayout()

        self.nameLine.addWidget(self.nameLable,2)
        self.pwdLine.addWidget(self.pwdLable, 2)
        self.captchaLine.addWidget(self.captchaLable, 3)

        self.nameLine.addWidget(self.nameEdit, 5)
        self.pwdLine.addWidget(self.pwdEdit, 5)
        self.captchaLine.addWidget(self.captchaEdit, 5)

        self.captchaLine.addWidget(self.codeLable, 5)

        self.nameLine.addWidget(self.nameTips, 5)
        self.pwdLine.addWidget(self.pwdTips, 5)
        self.captchaLine.addWidget(self.captchaTips, 5)

        self.totalLayout = QVBoxLayout()
        self.totalLayout.addLayout(self.nameLine)
        self.totalLayout.addLayout(self.pwdLine)
        self.totalLayout.addLayout(self.captchaLine)

        # Btn
        self.logBtn = QPushButton('登录', self)
        self.regBtn = QPushButton('注册', self)

        self.logBtn.setStyleSheet('background-color:#99CCFF; color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.regBtn.setStyleSheet('background-color:#99CCFF;color:rgb(0,0,0);font-size:26px;border-radius:5px')

        self.btnLine = QHBoxLayout()
        self.btnLine.addWidget(self.logBtn)
        self.btnLine.addWidget(self.regBtn)
        self.totalLayout.addLayout(self.btnLine)

        self.totalLayout.setContentsMargins(60, 250, 200, 30)
        self.setLayout(self.totalLayout)

        self.logBtn.clicked.connect(self.fLogin)    # 验证登录
        self.regBtn.clicked.connect(self.fLog2Reg)     # 注册


    # 刷新页面
    def paintEvent(self, QPaintEvent):
        # 给窗口设置背景图 画板、画刷、
        win_palette = QPalette()
        win_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("img/bgd.jpg").scaled(self.size())))
        self.setPalette(win_palette)


    # 回车登录
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.fLogin()


    # Tips
    def eventFilter(self, QObject, QEvent):
        if QObject == self.nameEdit and QEvent.type() == QEvent.FocusOut:
            if self.nameEdit.text() == '':
                self.nameTips.setText('用户名不能为空')
                return True
            elif self.nameEdit.text() not in self.userData.dData.keys():
                self.nameTips.setText('该用户不存在')
                return True
            else:
                self.nameTips.setText('')

        if QObject == self.pwdEdit and QEvent.type() == QEvent.FocusOut:
            if self.pwdEdit.text() == '':
                self.pwdTips.setText('密码不能为空')
                return True
            else:
                self.pwdTips.setText('')

        if QObject == self.captchaEdit and QEvent.type() == QEvent.FocusOut:
            if self.captchaEdit.text() == '':
                self.captchaTips.setText('验证码不能为空')
                return True
            else:
                self.captchaTips.setText('')
        return False


    # 跳转注册槽函数
    def fLog2Reg(self):
        self.reg.show()
        self.hide()


    # 注册返回登录槽函数
    def fReg2Log(self, str):
        self.reg.close()
        self.nameEdit.setText(str)
        self.show()


    # 验证登录槽函数
    def fLogin(self):
        self.user = self.nameEdit.text().strip()
        self.pwd = self.pwdEdit.text().strip()
        self.code = self.captchaEdit.text().strip()
        if self.user == '' or self.pwd == '':
            QMessageBox.information(self, '错误', '请输入信息')
        else:
            if self.user in self.userData.dData.keys():
                if self.pwd == self.userData.dData[self.user]:
                    if self.code == self.codeLable.text:
                        QMessageBox.information(self, '登录提示', '登录成功')
                        self.signalLog2Game.emit()
                    else:
                        QMessageBox.information(self, '登录提示', '验证码错误')
                        self.codeLable.updateCode()
                        self.captchaEdit.clear()
                else:
                    QMessageBox.information(self, '登录提示', '密码错误')
                    self.pwdEdit.clear()
            else:
                QMessageBox.information(self, '登录提示', '该用户不存在')
                self.nameEdit.clear()

