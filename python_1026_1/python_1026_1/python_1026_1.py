# 10월 26일 정규식(2)

## ex) findall 예제 
import re
#str = '''Window
#Unix
#Lunux
#Solaris'''

#p1 = re.compile('^.+',re.M) 
##줄바꿈을 제외한 한개의 문자 이상을 찾아낸다.M은 멀티라인을 제외한다. 
#print(p1.findall(str))

#p2 = re.compile('^.+',re.S)
#print(p2.search(str))
##명령만 search로 바꾼 경우 MultiLine을 적용해도 하나만 찾는다.

## ex) group 예제

#m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
#print(m.group('first_name','last_name')) # tuple 형태로 출력, group 하나만 출력도 가능 
#print(m.groupdict()) # 딕셔너리 형태로도 출력이가능

#m = re.match(r"(\d+)\.?(\d+)?","24")
#print(m.groups()) #두번째 그룹은 아무것도 없으므로 None으로 출력
#print(m.groups(0)) #디폴트 값 설정, 위처럼 두번째 그룹의 초기값을 0 으로 출력한다.

##Lookahead assertion

#p = re.compile(".+:")
#m = p.search("http://google.com")
#print(m.group()) 

##-> 결과는 http: 그러나 :을 제외하고 찾고싶다.

#p = re.compile(".+(?=:)") # 특정 문자열을 찾되, 그룹 전까지만 찾는다.
#m = p.search("http://google.com")
#print(m.group()) 

#import os
#os.chdir("C:\\") # 현재 디렉토리를 C\ 로 바꿈.
#print(os.getcwd())

#import glob

#print(glob.glob("*.*")) #현재 디렉토리의 모든 파일들을 리스트 형태로 반환
#files = glob.glob("*.*") #현재 디렉토리의 파일에 대해서도 정규식을 적용해보자.


##Lookbehind assertion

#p = re.compile("(?<=abc)def")
#m = p.search("abcdef")
#print(m.group())

#m = re.search('(?<=-)\w+', 'spam-egg') # 결과 egg, 하이픈 뒤의 문자열만 찾는다. 
#print(m.group())

#email = "tony@tiremove_thisger.net"
#m = re.search("remove_this", email)
#result = email[:m.start()] + email[m.end():] 
##그 문자열만을 뺀 결과만 반환, 여러개 있을 경우도 생각해보자
#print(result)

##포커

#def displaymatch(match):
#    if match is None:
#        return None
#    return '<Match: %r, groups=%r>' % (match.group(), match.groups())
#valid = re.compile(r"^[a2-9tjqk]{5}$")
#print(displaymatch(valid.match("akt5q")))
#print(displaymatch(valid.match("akt5e")))
#print(displaymatch(valid.match("akt")))
#print(displaymatch(valid.match("727ak")))

#Urllib

import urllib.request
with urllib.request.urlopen('http://www.python.org/') as f:
    text = str(f.read())
    p = re.compile("<title>+(\w+)+</title>")
    m = p.search(text)
    print(m)
    #print(f.read(300)) #300 byte
    #print(f.read(300).decode("utf-8")) #encoding mode utf-8