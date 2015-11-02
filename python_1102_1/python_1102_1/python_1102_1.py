
##test.xml
from bs4 import BeautifulSoup
#f = open('test.xml')
#xml = f.read()
#soup = BeautifulSoup(xml,"html.parser")
#for node in soup.findAll('node'):
#    print("Node : "+node.string) # 노드의 string
#    print("Attr1 : "+node['attr1']) # 노드의 attribute

##song.xml

#f = open('song.xml', encoding='utf-8') # 저장도 표기와 같은 형식으로 해야한다.
#xml = f.read()
#soup = BeautifulSoup(xml,"html.parser")
#for nodes in soup.test('song'):
#    for node in nodes:
#        print(node.string)

##alcohol.xml

#f = open('alcohol.xml', encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml,'lxml') # 파서를 지정할 수도 있다.
#for nodes in soup.alcohol('cate1'):

#    if( nodes["tt"] != "안주" ):continue

#    print('Cate1 :' + nodes['tt'],end="\n\n") # cate1 의 tt속성 접근
#    for node in nodes('cate2'): # cate1에 있는 cate2 태그 접근
#        print('\tCate2 : ' + node['tt'])
#        for item in node('item'):
#            print('\t\t\t' + item.string)


import json

#data = {1:'a',2:'b'}
#data2 = json.dumps(data)
#data3 = json.loads(data2)
#print(type(data2))# json 데이타는 str 타입으로 되어있다. 
#print(type(data3))# python 데이타는 dictionay 타입.

#data = {1:'우리',2:'나라'}
#data2 = json.dumps(data, ensure_ascii=False) # false 해줘야 오류 않남
#print(data2)

#s = """
#{
#"name": "cybaek",
#"detail" : { "last": "baek" },
#"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
#}
#""" # str 타입의 json 형태 

#data = json.loads(s) # json -> python dict
#print(data['name'])
#print(data['detail'])
#print(data['detail']['last'])

s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""
class JsonObject:
    def __init__(self, d):
        self.__dict__ = d
data = json.loads(s, object_hook=JsonObject) #직접 만든 json클래스를 넣을 수 있음.
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)