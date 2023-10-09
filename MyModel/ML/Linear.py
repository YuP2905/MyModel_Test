class Linear_Re:
    def __init__(self):
        self.name = '线性回归'
        pass
    def info(self):
        return f'{self.name}'
    pass

if __name__ == '__main__':
    l = Linear_Re()
    print(l.info())