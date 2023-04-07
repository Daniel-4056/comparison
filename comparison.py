import datetime
import numpy as np
a=np.random.randint(1,100,size=10000000,dtype=np.int64)
b=np.random.randint(1,100,size=10000000,dtype=np.int64)
def outter_decorator(func):
    def wraper(*args,**kwargs):
        start=datetime.datetime.now()
        func(*args,**kwargs)
        end=datetime.datetime.now()
        result=end-start
        print(f"time spended : {result}")
        return result
    return wraper


@outter_decorator
def pythonsum():
    for i,j in zip(a,b):
        python_sum=i*j
    return python_sum
        

    
@outter_decorator
def numpysum():
    return np.dot(a,b)



pythonsum()
numpysum()
       
