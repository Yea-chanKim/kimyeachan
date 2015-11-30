import numpy as np
from matplotlib import pyplot as plt

# 리스트의 내용을 추가시켜서 append 해줌
listData = [1,2,3]
#print(listData*2) 


data = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(data+2)      # 모든 인덱스에 2를 더함
#print(data*2)      # 모든 인덱스에 2를 곱함
#print(data*data)  # 같은 인덱스의 원소끼리 곱함
#print(data.dot(data)) # 실제 행렬 곱 

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

# 각 원소에 대해서 비교연산
#print(a == b) 
#print(a > b)

 # 전체 행렬에 대한 비교 연산
#print(np.array_equal(a,b))

#논리 연산
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
#print(np.logical_or(a, b))
#print(np.logical_and(a, b))

# 모든 원소 값이 True일때만 True
#print(np.all([True, True, True]))

# True인 원소가 하나라도 있으면 True
#print(np.any([True, True, False]))

# 초월함수 제공
#a = np.arange(1,5)
#print(a)
#print(np.sin(a))
#print(np.log(a))
#print(np.exp(a))

a = np.triu(np.ones((3, 3)), 1) 
# 두번째 인자 1은 인덱스 -> 어디서부터 채워진 삼각형을 만들것인가.
# 0은 대각선
#print(a)

# 모든 행렬 원소의 합을 구하는것
x = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
#print(np.sum(x))
#print(x.sum())

x = np.array([[1, 1],[ 2, 2]])
#print(x.sum()) # 전체 합 
#print(x.sum(axis=0)) #columns (first dimension) 열 합
#print(x.sum(axis=1)) #rows (second dimension) 행 합

x = np.array([1, 3, 2])
#print(x.min()) # value of minimum
#print(x.max()) # value of maximum
#print(x.argmin()) # index of minimum
#print(x.argmax()) # index of maximum

x = np.array([1, 2, 3, 4, 5])
y = np.array([[1, 2, 4], [5, 6, 1]])
#print(x.mean()) # 평균
#print(np.median(x)) # 중간값  n/2 의 원소 
#print(np.median(y, axis=-1))

data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T

print(data)

print("평균 : " + str(np.mean(data,axis=0)[1:4]))
print("표준편차 : " + str(np.std(data,axis=0)[1:4]))

(y, hare, lynex,carrot ) = np.argmax(data,axis=0)
print("산토끼 최대 : " + str(int(hare+1900)))
print("시라소니 최대 : " + str(int(lynex+1900)))
print("당근 최대 : " + str(int(carrot+1900)))

#plt.plot(year, hares, year, lynxes, year, carrots) # 3개의 그래프를 그림 (x,y) 순서쌍
#plt.show()



