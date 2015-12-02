import numpy as np
from matplotlib import pyplot as plt



##City 사이의 거리 구하기
#mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
#distance_array = np.abs(mileposts - mileposts[:, np.newaxis])

#print(mileposts[:,np.newaxis]) # newaxis 하면 세로축으로 나타냄
#print(distance_array)





#그리드 또는 네트워크 기반 거리 계산

## x는 가로, y는 세로로 되어 있는 data set(broadcasting)
#x,y = np.arange(5),np.arange(5)[:,np.newaxis]

#distance = np.sqrt(x**2+y**2)
## node 상의 거리를 구하는 행렬
#print(distance)

## 그래프 그리기
#plt.pcolor(distance)
#plt.colorbar()
#plt.show()

##ogrid 함수 사용
#x, y = np.ogrid[0:5, 0:5] #x : (5,1), y : (1,5) shape을 가짐

##mgrid 함수 사용 레이블
#x, y = np.mgrid[0:5, 0:5]

## Array Shape - Flattening
#a = np.array([[1, 2, 3], [4, 5, 6]])
#print(a.ravel()) #[1,2,3,4,5,6]
#print(a.T.ravel()) # [1,4,2,5,3,6]

## reshape
#b = a.ravel() 
#b = b.reshape((2, -1)) # 열에 해당하는 것은 명시 안해도 됨, -1을 주면 계산에 의해서 추정을 해줌
#print(b)


#z = np.array([1, 2, 3])
#print(z[:, np.newaxis]) # y 방향으로 바꿈
#print(z[np.newaxis, :]) # x 방향으로 바꿈

##Resizing
#a = np.arange(4) 
#print(a)
#a.resize((8,)) # 1x8 행렬
#print(a) # 빈부분은 0으로 채워짐

# sorting 
#a = np.array([[4, 3, 5], [5, 2, 1]])
#b = np.sort(a, axis=0) #Sorts each row separately!
## axis 0 => column sort axis 1 = > row sort
#a.sort(axis=1)
#print(a)
#print(b)

##sorting with index
#a = np.array([4, 3, 1, 2])
#j = np.argsort(a) 

#print(j) 
## 정렬된 인자들만 보여줌 
## arg sort는 원본은 정렬하지 않고, 정렬된 데이터를 반환한다.

#print(a[j]) 
## 정렬된 데이터 

#j_max = np.argmax(a) # finding maxima 
#j_min = np.argmin(a) # finding minima

## 방정식의 근 구 하기 
#p = np.poly1d([1, 2, 1])
#print(p) # 식
#print(p.roots) # 근 
#print(p.order) # 차원
#p = np.polynomial.Polynomial([1, 2, 1]) # 계수 값이 거꾸로 들어감


#x = np.linspace(0,1,20)
#y = np.cos(x) + 0.3*np.random.rand(20)
#p = np.poly1d(np.polyfit(x,y,3))
#print(x,y)
#print(p)
#t = np.linspace(0,1,200)
#plt.plot(x,y,'o',t,p(t),'-')
#plt.show()

## Chebyshev
#x = np.linspace(-1, 1, 2000)
#y = np.cos(x) + 0.3*np.random.rand(2000)
#p = np.polynomial.Chebyshev.fit(x, y, 90)
#t = np.linspace(-1, 1, 200)
#plt.plot(x, y, 'r.')
#plt.plot(t, p(t), 'k-', lw=3)
#plt.show()


#이미지 읽rl
img = plt.imread('woong.png')
print(img.shape, img.dtype)
print(img)
plt.imshow(img[0:300,0:450])

plt.show()