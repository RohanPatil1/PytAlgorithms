def isort(list):
    for j in range(1,len(list)):
        key=list[j]
        i=j-1
        while i>=0 and key<list[i]:
            list[i+1]=list[i]
            i=i-1
        list[i+1] = key
a=[1023,999,312,97,45,29,9,1]
isort(a)
print(a)

'''
#Making A Large List To Test
A=[]
n=0;m=0
for m in range(0,1001):
    A.append(m)
    m=m+1
    n=n+1


insertion_sort(A)
print A
'''
