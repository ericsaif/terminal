import numpy as np


x = np.array(list(range(0,3)))
av = np.average(x)
std=np.std(x)

print(av,std)