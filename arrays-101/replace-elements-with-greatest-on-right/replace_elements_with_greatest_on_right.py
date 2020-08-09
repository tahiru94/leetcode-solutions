def replace_elements_with_greatest_on_right(arr):
    for i in range(len(arr) - 1):
        arr[i] = max(arr[i + 1:])
    arr[-1] = -1
    return arr