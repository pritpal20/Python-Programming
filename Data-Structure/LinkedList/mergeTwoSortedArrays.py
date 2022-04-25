

l1 = [1,3]
l2 = [2]

# result should be [1,2,3]
def MergesortArrays(list1,list2):

    l3 = []

    j = 0
    i = 0
    while(i < len(list1) and j < len(list2)):

        if list1[i] < list2[j]:
            l3.append(list1[i])
            i+=1
        else:
            l3.append(list2[j])
            j+=1

    for i in range(i,len(list1)):
        l3.append(list1[i])

    for j in range(j,len(list2)):
        l3.append(list2[j])
    
    return l3


def findMedianSortedArrays(l3):

    len_a = len(l3)

    # print(len_a)


    odd = False
    middle = 0
    median = 0.0

    if len_a %2 == 1:
        odd = True
        len_a-=1
        index  = round(len_a /2  )
        median = l3[index] 
    else:
        middle = len_a / 2 

        # print(odd)
        index = round(middle)

        median = (l3[index -1 ] + l3[index] ) / 2

    return float(median)

    

l3 = MergesortArrays(l1,l2)

print(l3)

print(findMedianSortedArrays(l3))
