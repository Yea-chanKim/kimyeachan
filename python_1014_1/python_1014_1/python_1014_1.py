import re

#pattern = re.compile("d")
#result = pattern.search("dog")
#print(result)

#r1 = re.search("\\\\", "C:\\test")
#r2 = re.search(r"\\", "C:\\test") # 공백도 \(공백) 으로 해야하ㅡㄴ데 r 로하면 그냥 공백 가능

#print(r1,r2)

#str = '''sample1.
#sample2.
#sample3.'''

##print(str)

##p = re.compile('^.*',re.S)#시작 비교
#p = re.compile('.*$') #맨 뒤에서 부터 비교 
#result = p.search(str)
#print(result.group())

#str= '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)
#print(result.group(1))

str1 = "123126-1234567"
pattern = re.compile("(\d{6})+(-)+(\d{7})")
result = pattern.match(str1)

if(result != None):
    result2 = re.split(r'-',str1)
    print(result2)