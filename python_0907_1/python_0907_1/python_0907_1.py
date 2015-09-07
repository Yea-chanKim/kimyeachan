
#vs 는 cp949로 인코딩 모드가 되어있다.
'''
data = ['a','b','c',['abcd','efg']]

print(data[0])
print(data[-1][1])
'''


'''
list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1+list2
print(list3) # 리스트의 원소들을 합한다. 

list4 = list3*3
print(list4) # 리스트의 내용을 반복해서 저장


list1[0:1] = [7,8] # list[a:b] = a에서 시작하여 갯수가 b인 곳의 데이터를 수정하겠다. 즉, a<= x < b 인 범위에 대입을 한다.

list2[0] = [9,10] # 0의 인덱스에 '리스트'를 넣는다
print(list2)

list5 = []
list5.append(3)
print(list5)
'''
'''
list = [1,2,3,4,5]

listIndex = list.index(5) # 찾고자 하는 데이터의 인덱스를 반환을 한다.
print(listIndex)        # 인덱스를 이용해서 찾는 것은 리스트속의 리스트는 찾아주지 못한다. 
'''

'''
ListId = ['1qkqkrkawk','yeachan10','yeachankim']

ListId[0] = ['1qkqkrkawk',123123]
ListId[1] = ['yeachan10',4123]
ListId[2] = ['yeachankim',42451]

# Q. 리스트 속의 리스트에서는 리스트관련 함수를 못쓰는 것인가? - 가능하다!!!

ListId[0].append(["김예찬","010-2925-0191"])
ListId[1].append(["김예찬","010-2925-0191"])
ListId[2].append(["김예찬","010-2925-0191"])
'''

'''
for sindex in range(len(ListId)): # 인덱스를 가져오는 것     range(n) : 0 , 1, 2 ..., n-1 
    print(ListId[sindex])

for student in ListId: # 리스트에 해당하는 값을 하나씩 가져오는 것 
    print(student)
'''

''' 상위 5개의 항목 출력 
unsortedList =  [31,32,5,3,1,7,99]
unsortedList.sort()
unsortedList.reverse()

top5List = unsortedList[0:5]
print(top5List)
'''