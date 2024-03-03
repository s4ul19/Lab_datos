from matplotlib import pyplot 
import math
import pandas as pd
import numpy as np

def binomial(x,n,p,q):
    comb= math.comb(n,x)
    p_x=p**x 
    q_nx=q**(n-x)
    return comb*p_x*q_nx

n=50
lista=np.arange(n+1)
data_table=pd.DataFrame({'x':lista})

q=1/2
p=1/2
data_table['Pb']= data_table.apply(lambda row: binomial(row['x'],n,p,q),axis=1 )
print(data_table)