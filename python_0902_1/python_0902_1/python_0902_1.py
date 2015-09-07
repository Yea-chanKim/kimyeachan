
#print("first {0:3d} second {1:3d}".format(3))


#print("한글")


'''

first = input("your first number : ")
second = input("your second number : ")

fisrtint = int(first)
secondint = int(second)

print("sum : %d" %(fisrtint+secondint))

'''

'''

forround = float(input("float : "))
print(round(forround,1))

'''

'''

fortypechecking = "string"
print(type(fortypechecking))

'''

'''
"와 '를 구분해서 사용하면 된다!

print("it's a chicken")

'''

''' 0 -> 시작,  -1 -> 끝 을 지정하는 index이다.

str = "greenjoa"
print(str[-2])

'''

''' 문자열 슬라이싱

str = "12345김예찬"
print (str.endswith)

print(len("gsdsdgsdg"))

'''

''' 문자열 줄맞춤 

print("I eat %10s apples." % "five")
print("I eat %-10s apples." % "five")

'''



isEnd = input("종료할까요?")

isEndLower = isEnd.lower();

if(isEndLower == "yes"):
    print("종료합니다")
elif(isEndLower == "no"):
    print("종료안합니다.")
else:
    print("이상합니다")