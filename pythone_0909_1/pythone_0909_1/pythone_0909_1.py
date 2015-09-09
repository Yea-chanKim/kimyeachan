
''' #dictionary
a = {'name':'pey','phone':'0119993323'}

keyList = list(a.keys()) # key값만 뽑아 리스트로 만든다.
                         # value로 하려면 a.values() 로 하면 된다. 
print(a.items()) # tuple로 묶은 값을 반환 한다. 

print(a.get('name')) # key값으로 value에 접근 


adic = {'green':{'홍길동':'5.5'}}

print(adic.get('green').get('홍길동')) # value에도 dictionary가 저장되어 있을 수가 있다. 
                                       # 리스트안 리스트에서는 이차원 배열처럼 접근

'''

'''
s1 = set([1,1,1])

print(s1) # sets는 중복을 허락하지 않는다. 
'''

##제어문##

'''
answer = input("Would you like express shipping?")
if answer.lower() == "yes" : # lower는 입력받은 string을 모두 소문자로 바꿔준다.
    print("That will be an extra $10")
if( 'y' in answer.lower()):
    print("That will be an extra $10")
'''

'''
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
'''

'''#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print("%d*%d=%d\t"%(i,j,i*j),end=" ")
        
    print("")
'''

import turtle

nSides = 5
for steps in range(nSides):
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides) :
        turtle.forward(10)
        turtle.right(360/nSides)


inputs = input("22")