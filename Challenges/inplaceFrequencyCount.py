def inplace_count(nums):
	"to mark which slot has been occupied by freq, "
    "let's use negative number to do counting"
    for i in range(len(array)):
        if array[i] > 0:
            val = array[i]
            if array[val] < 0:
                # array[val] already occupied by freq
                array[val] -= 1
            else:
                # if array[val] haven't been processed yet
                # let's swap it out
                temp = array[val]
                while array[temp] > 0:
                    new_temp = array[temp]
                    array[temp] = -1
                    temp = array[new_temp]
                array[temp] -= 1
    
    # to respect "inplace", so we don't use list-comp here
    for i, v in enumerate(A):
        if v >= 0:
            A[i] = 0
        else:
            A[i] = -A[i]
    return array
