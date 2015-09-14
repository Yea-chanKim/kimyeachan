def printRecursiveList(mlist,level = 0):
    for item in mlist:
        if(isinstance(item,list)):
            printRecursiveList(item,level+1)
        else:
             for idx in range(0,level):
                 print('\t',end="")
             print(item)
