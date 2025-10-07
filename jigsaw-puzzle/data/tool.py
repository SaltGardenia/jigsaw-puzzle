class data():
    # 初始化用户数据
    def __init__(self):
        self.dData = {}
        with open('data/data.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                data = line.split(',')
                self.dData[data[0]] = data[1]
    # 存储用户数据
    def saveUserData(self):
        with open('data/data.txt', 'w') as f:
            for item in self.dData:
                string = item + ',' + self.dData[item] + '\n'
                f.write(string)

