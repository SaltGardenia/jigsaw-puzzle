from view.loginWidget import *
# 注册页
class regWidget(QWidget):
    signalReg2Log = pyqtSignal(str)      # 注册返回登录信号
    def __init__(self, userData, width = 1000, height = 600):
        super().__init__()
        self.width = width
        self.height = height
        self.cData = userData
        self.data = userData.dData

        self.setWindowTitle('注册窗口')
        self.resize(self.width, self.height)
        self.setWindowIcon(QIcon('img/icon.png'))

        win_palette = QPalette()
        win_palette.setBrush(self.backgroundRole(), QBrush(QPixmap('img/bgd.jpg').scaled(self.size())))
        self.setPalette(win_palette)

        # Lable
        self.nameLable = QLabel('用户名', self)
        self.pwdLable = QLabel('密码', self)
        self.repwdLable = QLabel('确认密码', self)

        self.nameLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')
        self.pwdLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')
        self.repwdLable.setStyleSheet('color:white; font-size:22px; font-weight:bold')

        # Edit
        self.nameEdit = QLineEdit('', self)
        self.pwdEdit = QLineEdit('', self)
        self.repwdEdit = QLineEdit('', self)

        self.nameEdit.setPlaceholderText('请输入6-10位用户名')
        self.pwdEdit.setPlaceholderText('请输入密码')
        self.repwdEdit.setPlaceholderText('请确认密码')

        self.nameEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')
        self.pwdEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')
        self.repwdEdit.setStyleSheet('height:50px; color:#666666; border-radius:5px; font-weight:bold;font-size:22px')

        self.pwdEdit.setEchoMode(QLineEdit.Password)
        self.repwdEdit.setEchoMode(QLineEdit.Password)

        # Btn
        self.regBtn = QPushButton('注册', self)
        self.retBtn = QPushButton('返回', self)

        self.regBtn.setStyleSheet('background-color:#99CCFF;color:rgb(0,0,0);font-size:26px;border-radius:5px')
        self.retBtn.setStyleSheet('background-color:#99CCFF;color:rgb(0,0,0);font-size:26px;border-radius:5px')

        # Layout
        self.nameLine = QHBoxLayout()
        self.nameLine.addWidget(self.nameLable, 1)
        self.nameLine.addWidget(self.nameEdit, 7)

        self.pwdLine = QHBoxLayout()
        self.pwdLine.addWidget(self.pwdLable, 1)
        self.pwdLine.addWidget(self.pwdEdit, 7)

        self.repwdLine = QHBoxLayout()
        self.repwdLine.addWidget(self.repwdLable, 1)
        self.repwdLine.addWidget(self.repwdEdit, 7)

        self.btnLine = QHBoxLayout()
        self.btnLine.addWidget(self.regBtn, 1)
        self.btnLine.addWidget(self.retBtn, 1)

        self.totalLayout = QVBoxLayout()
        self.totalLayout.addLayout(self.nameLine)
        self.totalLayout.addLayout(self.pwdLine)
        self.totalLayout.addLayout(self.repwdLine)
        self.totalLayout.addLayout(self.btnLine)

        self.totalLayout.setContentsMargins(60, 250, 600, 0)
        self.setLayout(self.totalLayout)

        # 信号连接
        self.retBtn.clicked.connect(self.fReg2Log)
        self.regBtn.clicked.connect(self.fReg)


    def paintEvent(self, QPaintEvent):
        # 给窗口设置背景图 画板、画刷
        win_palette = QPalette()
        win_palette.setBrush(self.backgroundRole(), QBrush(QPixmap("img/bgd.jpg").scaled(self.size())))
        self.setPalette(win_palette)


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.fReg()


    # 注册返回登录槽函数
    def fReg2Log(self):
        self.nameEdit.clear()
        self.pwdEdit.clear()
        self.repwdEdit.clear()
        self.signalReg2Log.emit('')


    # 验证注册函数
    def fReg(self):
        user = self.nameEdit.text().strip()
        pwd = self.pwdEdit.text().strip()
        repwd = self.repwdEdit.text().strip()
        if user == '' or pwd == '' or repwd == '':
            QMessageBox.information(self, '错误', '请输入信息')
        else:
            if user not in self.data:
                if pwd == repwd:
                    self.data[user] = pwd
                    QMessageBox.information(self, '注册提示', '注册成功')
                    self.cData.saveUserData()
                    self.signalReg2Log.emit(user)
                else:
                    QMessageBox.information(self, '注册提示', '密码不一致')
            else:
                QMessageBox.information(self, '注册提示', '该用户已存在')