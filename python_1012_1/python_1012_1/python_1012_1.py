
import os 
import sys

#os.system("python test.py a b c")
#print(sys.path)

class student:
    def __init__(self,inName,inAge):
        self.name = inName
        self.age = inAge
    
    def show(self):
        print(self.name + " : " + str(self.age))

std1 = student("홍길동",22);
#std1.show()

#이 객체를 그대로 저장하고 싶으면? 
import pickle
#f = open("test.txt","wb")
#pickle.dump(std1,f)
#f.close

#f = open("test.txt","rb")
#data = pickle.load(f)
#data.show()
#f.close

#print(os.environ)
#os.chdir("..")
#print(os.getcwd())
#print(list(os.walk('..')))

#for (path, dir, files) in os.walk('..'):
#    for filename in files:
#        print(filename)

# sample이라는 디렉토리를 만들고, 
# 이곳에 txt파일로 복사를해라

#import shutil
#if( os.path.isdir("sample") == False ): # exist 함수로도 확인 가능 
#    os.mkdir("sample")

#for (path, dir, files) in os.walk('.'):
#    for filename in files:
#        flist = filename.split(".")
#        if( flist[1] == "txt" ):
#            shutil.copy(filename,"sample/"+filename)
        

#print(os.path.dirname('c:/python34/python.exe'))