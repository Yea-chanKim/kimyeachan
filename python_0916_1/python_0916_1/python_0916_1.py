## with 구문을 쓰면 close를 해줄 필요가 없다.
## 그러나 다른 방식인 경우 open했으면 close 해야한다

## w+로 하면 기존파일 없어지고 새로만들어진다.
#   #for line in myfile:# 기본 단위가 라인단위로 읽는다. 
#        #print(line)
    

#fileName = "파일입출력예제2.txt"
#lists = []
#with open(fileName,"r") as myfile:
#    #content = myfile.read()
#    #print(content)

#    while True:
#        content = myfile.readline()
#        if not content : break
#        lists.append(content)

#monicaEtc = []
#roleList = []
#fileNewName = "monica.txt"

#for i in range(0,len(lists)):
#    (role,etc) = lists[i].strip().split(":",1)
#    # max split의 값 - 몇개까지 나눌 것이냐, 몇번째 등장부터 나눠주는가
#    roleList.append(role)
#    if(role.lower() == "monica"):
#        monicaEtc.append(etc)

#import pickle 

#with open(fileNewName,"wb") as myfile2:
#    #for i in range(0,len(monicaEtc)):
#    #    myfile2.write("Monica : "+monicaEtc[i]+"\n")
#    pickle.dump(roleList,myfile2)

##print(roleList)

#with open(fileNewName,"rb") as monica:
#    result = pickle.load(monica)
#    print(result)


# # 리스트의 형태 그대로 -> 파일, 파일 -> 리스트의 원형으로 불러와주는 라이브러리

## dump -> 파일에 저장 , read -> 읽어오는 것 ,대신 읽고 쓰는 모드가 binary상태이므로 뒤에 b를 붙여줘야한다. wb, rb
