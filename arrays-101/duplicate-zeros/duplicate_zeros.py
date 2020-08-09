def duplicate_zeros(arr):
    if 0 not in arr:
        return arr
    else:
        array = []
        for a in arr:
            if a == 0:
                array.extend([0, 0])
            else:
                array.append(a)
        for i in range(len(arr)):
            arr[i] = array[i]