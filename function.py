import numpy as np
import random
def make_distribution(k):
    return [random.random() for i in range(k)]

def UCBi(each_attempt,each_result,i):
    k = 2 ; d = 0.05 
    return each_result[i]/each_attempt[i] + np.sqrt(0.5*np.log(2*k*each_attempt[i]**2/d)/each_attempt[i])

def LCBi(each_attempt,each_result,i):
    k = 2 ; d = 0.05 
    return each_result[i]/each_attempt[i] - np.sqrt(0.5*np.log(2*k*each_attempt[i]**2/d)/each_attempt[i])

def max_idx(list,a1 = None):
    if a1 is not None:
        list[a1] = 0
    return [i for i in range(len(list)) if max(list)==list[i]]