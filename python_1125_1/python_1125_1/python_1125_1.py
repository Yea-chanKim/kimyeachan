import numpy as np



# 그래프 그릴때 사용하는 것 ( Matplotlib )
# numpy 설치 후 -> matplotlib 설치 



## 행렬 생성 및 타입 변환
#data = np.array([[1,2,3],[4,5,6],[7,8,9]])
#data.astype(np.float)


## 단위 행렬 생성 및 전치 행렬(단위 벡터에 대해선 변화 x)
#earray = np.eye((3))
#print(earray.T) 
#print(earray)

##등간격 배열 만들기 
#data = np.arange(10)
#data = np.arange(10,1,-1) #start, end(exclusive), step - 열이 증가하는 형태
#np.arange(10,1,-1)[:, np.newaxis] #행증가
##print(data)

#data = np.arange(35).reshape(5,7) # 행렬 형태를 5x7 로 바꿔줌, 데이터 갯수와 딱맞아야함
##print(data)

#data = np.linspace(1., 4., 6,endpoint = False) #start, end, num-points
##print(data)

## 난수 생성
#data = np.random.randn(4,4) # rand한 수가 들어가는 4*4 행렬
##print(data)

##데이터 읽고 출력
#data = np.loadtxt('data.txt')
##print(data)
##print(data[0])            # 첫번째 행 출력 
##print(data[0:2])        # 첫번째 행 출력  start:end(exclusive)
##print(data[1:4:2])    # start:end:step
##print(data[::-1])      # 행을 reverse하여 출력

#x = np.arange(10,1,-1)
##print(x)
##print(x[np.array([[1,1],[2,3]])]) # x의 index를 통해 새로운 배열 생성

#y=np.arange(35).reshape(5,7)
##print(y)
##print(y[np.array([0,2,4])])

#b = y>20 # 조건이 들어갈 수 도 있음 
##print(y[b])

# 마스크 - 인덱싱 슬라이싱
data = np.arange(36).reshape(6,6)
#mask=np.array(np.array([1,0,1,0,0,1],dtype=bool))
#print(data)
#print(mask)
#print(data[mask,2]) # 2열에 대해서 마스크를 씌움(↓)

mask1=np.array([0,1,2,3,4])
mask2=np.array([1,2,3,4,5])
#print(data[mask1,mask2]) # (0행 1열), (2행 2열) ... (4행 5열) 로 가져온다.

mask1 = np.array([3,4,5]) # 파란 부분 뽑기
mask2 = np.array([0,2,5])
print(data[mask1,mask2])