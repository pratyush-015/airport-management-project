import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np
def GRAPH_MENU():
    L1={'No of pssg boarded':[34,12,20,12,10,17,11],'No of employees present':[12,43,19,24,19,48,38],'No of cancelled ticket':[10,5,9,6,13,12,5],'No of new tickets':[13,14,6,8,24,34,12]}
    S1=pd.DataFrame(L1,index=['Monday', 'Tuesday ','Wednesday ','Thursday ','Friday ','Saturday ','Sunday '])
    print(S1)
    X= np.arange(0,7)
    plt.bar(X,S1['No of pssg boarded'], width=0.25,label='No of pssg boarded')
    plt.bar(X+0.25,S1['No of employees present'], width=0.25,label='No of employees present ')
    plt.bar(X+0.50,S1['No of cancelled ticket'], width=0.25,label='No of cancelled ticket')
    plt.bar(X+0.75,S1['No of new tickets'], width=0.25,label='No of new tickets')
    plt.legend(loc=1)
    S1.plot.bar()
    S1.plot()
    plt.show()
