import numpy as np

data = np.array([np.arange(0, 60, 10)]).T 
# [] 를 꼭 해줘야 벡터에 T연산이 가능하다!!
add = np.array(np.arange(0,6))
print(data+ add)
