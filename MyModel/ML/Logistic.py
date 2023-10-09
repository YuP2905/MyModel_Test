class Logistic_Re:
    def __init__(self):
        self.__name = '逻辑回归'
        pass
    def info(self):
        return f'{self.__name}'
    pass

if __name__ == '__main__':
    p = Logistic_Re()
    print(p.info())