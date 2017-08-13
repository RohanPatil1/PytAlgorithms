import time

def partition(list1):
    left,right = [],[]
    pivot=list1[len(list1)-1]
    for i in range(len(list1)-1):
        element=list1[i]
        if element<=pivot:
            left +=[element]
        else:
            right +=[element]

    return (left,pivot,right)

def quick_sort(list1):

    if len(list1)<2:
        return list1

    else:
        (left,pivot,right)=partition(list1)
        sorted_left=quick_sort(left)
        sorted_right=quick_sort(right)
        #print (sorted_left+[pivot]+sorted_right)
        return (sorted_left+[pivot]+sorted_right)





a = [1023, 999, 312, 1000, 97, 45, 29, 9, 1, -1, 12]

print quick_sort(a)
