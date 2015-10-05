
def Assign2_():
    fileName = "201401.txt"
    checkOutList = []
    fieldList = []
    findList = []

    try:
        with open(fileName, "r") as myFile:
    
            while True:
                content = myFile.readline()
                if not content:break

                nlist = content.split("|") # list로 분할
                checkOutList.append(nlist)

                if( fieldList.count(nlist[2]) == 0 ): # 필드 리스트에 추가 (중복방지)
                    fieldList.append(nlist[2])
            
    
        for fidx in fieldList:
            print(fidx,end ="\t")

        keyValue = input("찾고자 하는 3번째 필드명 : ")

        for i in checkOutList :
            if( i[2].lower() == keyValue.lower()): # 찾는 필드명만 구분
                findList.append(i)



        import xlsxwriter

        workbook = xlsxwriter.Workbook('GB.xlsx')
        worksheet = workbook.add_worksheet("sheet")

        row = 0

        for i in findList:
            worksheet.write(row,0,i[0])
            worksheet.write(row,1,i[1])
            worksheet.write(row,2,i[2])
            worksheet.write(row,3,i[3])
            row += 1

        print("%d개의 데이터 출력 완료" %(len(findList)))
        workbook.close()
    except:



