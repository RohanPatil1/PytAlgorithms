a = [1023, 999, 312, 1000, 97, 45, 29, 9, 1, -1, 12]


def merge(left, right):
    result = []
    i ,j = 0, 0

    # -----Check  If  Both Of Them Have Any Data------------------------------#
    while i < len(left) and j < len(right):

        # ----------------If  Both Of Them Have Any Data------------------------------#
        # --------Compare the list items and append the smaller of them to our output-----#
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        # ----------------Add the Last Remaining Term From Any Of The Possible Left Two List --------------------#
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    # ----------------If The List Has Only ONE Term Then It is Already Sorted------------------------------#
    if len(list) < 2:
        return list
    middle = len(list) / 2

    # Here Is The Magic Of MergeSort Happens------First we call our both UNSORTED HALF HERE, Taking One Of The List As Example-->
    #       Our list gets divided into a list whic contains single Terms And Then recursively gets added back into the itself but THIS TIME SORTED....

    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    #print merge(left, right)
    return merge(left, right)

a = [1023, 999, 312, 1000, 97, 45, 29, 9, 1, -1, 12]
print mergesort(a)
