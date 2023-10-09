class ANN:
    def  __init__(self):
        self.__name = '全连接神经网络'
        pass

    def __str__(self):
        return f'{self.__name}'
        pass
    pass

if __name__ == '__main__':
    ann = ANN()
    print(ann)