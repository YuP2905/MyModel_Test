from ML.Logistic import Logistic_Re
from DL.ANN import ANN

log = Logistic_Re()
ann = ANN()
print(f'{ann}可以看做是多个{log.info()}的叠加')