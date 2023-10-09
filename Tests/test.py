import MyModel as my
import MyModel.AI.Info as info
from MyModel.ML.Logistic import Logistic_Re
from MyModel.DL.ANN import ANN
from MyModel.Calculation  import *


if __name__ == '__main__':
    pi = my.math.pi 
    ai = info.AI_Info()
    log = Logistic_Re()
    ann = ANN()
    res_1  =  ADD.nums_add(5,6)
    ## res_2 = SUB().nums_add(3,5)  ### 会报错, 因为__all__魔术变量里没有'SUB'模块
    list_test = [pi, ai, log.info(), ann, res_1]
    for item in list_test:
        print(item)