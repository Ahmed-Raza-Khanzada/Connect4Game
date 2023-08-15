#Practice code
class A:
     def __init__(self):
          self.b  =4
a = A()
print(a.b)

quit()
import numpy as np
import random
a = [[1, 2, 3,0],
     [0, 1, 4, 0],
     [3, 0, 0, 6],
     [4, 0, 2, 3]]
def n(mat):
    array = np.array(mat)
    l = (1,2,3,4)
    for i in array:
        for pos,j in enumerate(i):
          if j==0:
            while True:
               for r in l:
                    if r not in i and r not in array[:,pos]:
                         print(i,array)
                         print(r)
                         break
                    break   

n(a)
# a = np.array(a)
# print(a[:,0])