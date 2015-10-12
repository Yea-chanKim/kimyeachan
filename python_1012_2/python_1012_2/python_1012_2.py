#import glob

#print(glob.glob('*.py'))#현재 디렉토리에 .py로 만들어진 파일을 찾아 반환한다.

#print(glob.glob('./[0-9].*'))

#import glob,os.path

#ndir = nfile = 0

#def traverse(dir,depth):
#    global ndir,nfile
#    for obj in glob.glob(dir+'/*'):
#        if depth == 0:
#            prefix = '|--'
#        else:
#            prefix = '|'+' ' *depth+'|--'
#        if os.path.isdir(obj):
#            ndir+=1
#            print(prefix + os.path.basename(obj))
#            traverse(obj,depth+1)
#        elif os.path.isfile(obj):
#            nfile+=1
#            print(prefix + os.path.basename(obj))
#        else:
#            print(prefix + 'unknown object ',obj)

#            if __name__ == '__main__':
#                traverse('..',0)
#                print('\n',ndir,'directories,',nfile,'files')

#traverse('C:\\python34',0)
#if __name__ == '__main__':
#    traverse('..',0)
#    print('\n',ndir,'directories,',nfile,'files')

#import tempfile as tf

#with tf.TemporaryFile('w+',delete = True) as fp:#False로 주면 삭제되지 않는다. 
#    fp.write('Hello world!')
#    fp.seek(0)
#    print(fp)
#    data = fp.read()

#import time #시간 형식을 우리가 원하는대로 만들 수 있어야한다.

##time.time() # 현재 시간을 얻는 함수 
#t1 = time.ctime(time.time())
#ts = time.strptime(t1) #struct타입으로 만들어주는 함수

#print(t1)
#print(ts) #시간 객체를 분리해서 struct형태로 만들어준다.

##print(time.strftime("%B %dth %A %I:%M", time.localtime()));
##print(time.time())

import calendar


#calendar.prcal(2015)

#(wm,y) = calendar.monthrange(2015,10)
#print(wm)
#print(y)

import random

#arr = random.sample(range(0,100),10)
#print(arr)
#random.shuffle(arr)
#print(arr)
#print(random.choice(arr))

#colors = [('Red',3),('Blue',1),('Yellow',2),('Green',4)]
#p = []
#for val,cnt in colors:
#    for i in range(cnt):
#        p.append(val)


#random.shuffle(p)
#print(random.choice(p))

#import webbrowser
#url = 'http://google.com'
#webbrowser.open_new_tab(url)
#webbrowser.open_new(url)

