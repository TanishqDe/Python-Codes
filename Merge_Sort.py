def merging(A,B):
    (c,m,n)=([],len(A),len(B))
    (i,j)=(0,0)

    while ((i+j)<(m+n)):
        if(i==m):
            c.append(B[j])
            j=j+1
        elif(j==n):
            c.append(A[i])
            i=i+1
        elif(A[i]<=B[j]):
            c.append(A[i])
            i=i+1
        elif (A[i] > B[j]):
            c.append(B[j])
            j = j + 1
    return(c)

def mergesort(list1,left,right):
    if right-left <= 1:

        return(list1[left:right])

    elif (right-left) > 1:

        mid = (right+left)//2

        L = mergesort(list1, left, mid)
        R = mergesort(list1, mid, right)

        return(merging(L,R))


list2 = [3,2,5,7,8,9,4,11]

print(mergesort(list2,0,len(list2)))





