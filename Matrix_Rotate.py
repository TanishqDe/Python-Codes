def rotate(list):
    l=len(list)
    t=len(list[0])
    list2=[]
    list1=[]

    for i in range(0,len(list)):
        for j in range(0,len(list[0])):
            list1.append(list[(l - j - 1)][i])


    matrix = []
    for i in range(0, len(list1), t):
        matrix.append(list1[i:i + t])

    return(matrix)


rotate([[1,1,1],[2,2,2],[3,3,3]])
