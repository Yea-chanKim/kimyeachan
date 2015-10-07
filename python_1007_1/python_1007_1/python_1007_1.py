

# https://wikidocs.net/32 참고

#ata = ['abc',123,42323,'2324']
#print(dir(data))


#data2 = list(enumerate(data))
#print(data2) # 시퀀스형 자료형을 열거체로 만들어준다. 


#print(eval('1+2')) #연산 가능한 문자열을 넣으면 실행결과를 반환해준다.


#def f1(l):
#    return not l%2
#data = [1,2,3,4,5,6,7,8]
#print(list(filter(f1,data))) #짝수만 출력하는 함수 


#data = [1,2,3,4,5,6,7,8]
#print(id(data))
#for i in data:
#    print(id(i))


#data = [1,2,3,4,5,6,7,8]
#print(list(filter(lambda x: x%2==0,data)))


#a = [1,2,3] 
#b = list(a) # 새로운 참조형 데이터를 만듦
#c = a 

#print('a 의 ID : ' + str(id(a)))
#print('b 의 ID : ' + str(id(b)))
#print('c 의 ID : ' + str(id(c)))

##파이썬에서의 자료형은 모두 참조형이므로  
##대입 연산자가 일어나면 얕은 복사가 수행된다.

#def two_times(x):return x*2

#print(list(map(two_times,[1,2,3,4])))

#print( eval(repr("hi".upper())))
##print( eval(str("hi".upper()))) -> 에러가 발생한다. 

#data = [1,24,3,5,24,5]
##data.sort() # 실제 값을 정렬을 함.
#print(sorted(data)) #실제 값을 정렬하지는 않음 복사본 반환
#print(data)


#print(list(zip([1,2,3], [4,5,6], [7,8,9])))
#print(list(zip("abc", "def")))

data = {
    '홍길동' :[80,70,60,92],
    '김길동' :[24,35,18,10],
    '고길동' :[14,64,42,31]
        }

for ld in data.keys():
    data[ld].sort()

key_list = list(data.keys())
key_list.sort()

data3 = sorted(data, key=data.get)
print(data3)
#print(data.keys())
#for idx in range(0,len(key_list)):
#    for idx2 in data.keys():
#        data[idx2] = data[key_list[idx]]

#print(data)
#print(data.get('홍길동'))
#while(1) :
#    print(list(data.keys()))
#    key = input('이름을 입력 : ')
#    print(data[key])