#class A():
#    def __init__(self,a):
#        self.a = a

#    def show(self):
#        print('show',self.a)


#class B(A):
#    def __init__(self,b,**arg):
#        super().__init__(**arg)
#        self.b = b

#    def show(self):
#        print('show',self.b)
#        super().show()

#class C(A):
#    def __init__(self,c,**arg):
#        super().__init__(**arg)
#        self.c = c

#    def show(self):
#        print('show',self.c)
#        super().show()

#class D(B,C):
#    def __init__(self,d,**arg):
#        super().__init__(**arg)
#        self.d = d
#    def show(self):
#        print('show',self.d)
#        super().show()

#data = D(a=1,b=2,c=3,d=4)
#data.show()



#class Mapping:
#    def __init__(self,iterable):
#        self.item_list = []
#        self.__update(iterable) # 외부에서 접근이 불가능하도록함

#    def update(self,iterable):
#        for item in iterable:
#            self.item_list.append(item)
#            print('1',item)
#    __update = update # private copy 

#class MappingSubclass(Mapping):

#    def update(self,keys,values):
#        for item in zip(keys,values):
#            self.item_list.append(item)
#            print('2',item)


#tlist = [1,2,3,4,5]

##m2 = Mapping(tlist)
##m2.update(tlist)


#m1 = MappingSubclass(tlist)
#m1.update([1,2,3],['a','b','c'])


#import sys

#n1 = float(input("enter a number : "))
#n2 = float(input("enter a number : "))

#try:
#    result = n1 / n2
#    print(result)

#except:
#    err = sys.exc_info()[0]
#    print(err)
#    sys.exit()
#finally:
#    print('Done')

import Assign2_

Assign2_.Assign2_()