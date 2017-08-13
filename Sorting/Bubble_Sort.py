lst=[3,1,4,0]

for j in range(0,len(lst)-1):
    check_swap = False
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1]:
            swap = lst[i]
            lst[i] = lst[i+1]
            lst[i + 1] = swap

            check_swap =True
    if check_swap == False:
        break

    print (j,lst)
