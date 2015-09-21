
class Movie:
    '''영화 클래스''' # 긴문자열 처리할 떄 
    count = 0 # 별도의 메모리를 갖게 됨 객체를 만들 때 마다
    title = ""
    dir = ""

    def __init__(self,title,dir):# __는 시스템에서 약속된 함수
        self.title = title
        self.dir = dir
        self.__class__.count += 1 # 내 인스턴스가 아닌 클래스에 내장되어 있는 것을 증가시킨다.
        #self.count += 1 # 인스턴스를 생성할 떄 마다 별도의 메모리를 만들어서 공용으로 사용할 수 없다.
        print(self.title + " 생성자 호출")


    def printInfo(self):#함수 맨앞의 인자는 self
        print(self.title)
        print(self.dir)

    def __del__(self):
        print(self.title + " 소멸자 호출")
        
    @staticmethod
    def showCount1():
        print(Movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)





#m1 = Movie("김또깡","김두환")
#m1.mainActor = "김두환" #m1만의 변수 

#print("m1의 주인공 %s" %(m1.mainActor))


#m2 = Movie("김용석","용석이")

##print("m2의 주인공 %s" %(m2.mainActor))

#Movie.__init__(m3,"작두","계작두")

#m3.printInfo()

#m1 = Movie("베테랑","류승완")
#print(m1.title)
#print(m1.__doc__) # 클래스에 대한 설명 


#m1 = Movie("암살1","김태호1")
#m2 = Movie("암살2","김태호2")
#m3 = Movie("암살3","김태호3")
#m4 = Movie("암살4","김태호4")

#print(type(m4))
#m4 = m3 # 모든 변수는 참조형이므로, 대입연산을 하면 같은 주소를 가르키고 있는 형태가 된다
#        # 깊은 복사가 아닌 얕은 복사가 일어난다.

#print(id(m4))
#print(id(m3)) # 같은 주소를 가르키고 있다. ㅁ

#m4.printInfo()

m1 = Movie("트랜스포머1", "마이클베이")
m2 = Movie("트랜스포머2", "Michael Bay")
m3 = Movie("트랜스포머3", "Michael B")
m4 = Movie("트랜스포머4", "M Bay")

Movie.showCount2()
Movie.showCount1()
print(m1.count)
