#imports of outside libraries
import numpy as np
import matplotlib.pyplot as plt
#----------
inp=input('what # am i thinking of from 1-10:')
if inp==5:
    print('True')
else:
    print('False')    
    k=input('try again:')
    if k==5:
        print('True')
    else:
        print('False')
if inp == 4:
    print('Very Hot')
else:
    print ('False')

x=np.array([1,2,3,5,7,3])
y=np.array([3,2,4,5,3,2])
plt.plot(x,y)
plt.show()