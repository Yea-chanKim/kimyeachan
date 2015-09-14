
''' # 정의되는 부분이 위로 올라가야한다. 
    # main함수를 만들어서 다른 위치의 함수를 main에서 호출해주면 된다. (꼼수이긴함)
def helloPrint():
    print("Hello World ")
    return



helloPrint()
'''

'''
#여러개의 값을 반환화도록 하면, 하나의 묶음(Tuple)형태로 묶어서 반환을 하게 된다.

def MultiReturn(): 
    a = 1
    b = "222"
    return a,b


c,d = MultiReturn()

print(c)
print(d)

e = MultiReturn()
print(e[0])
print(e[1])
'''

#coding:cp949 
# -> 유니코드를 cp949로 인코딩 모드를 바꿔줌. 

''' # 리스트 안에 리스트 출력
def printMovieList(mlist):
    for item in mlist:
        if(isinstance(item,list)):
            for items in item:
                print(items)
        else:
            print(item)
'''
'''
def printRecursiveList(mlist,level = 0):
    for item in mlist:
        if(isinstance(item,list)):
            printRecursiveList(item,level+1)
        else:
             for idx in range(0,level):
                 print('\t',end="")
             print(item)



mlist = ["오이",["애호박","김치",["가지"]],"오징어",["삼치"]]

printRecursiveList(mlist)

'''
'''
import printData 

printData.printRecursiveList(mlist) 
'''
import os
print(os.getcwd())
#os.mkdir("sample")
os.chdir("./sample")
#os.system("python setup.py sdist") 
os.system("python setup.py install")