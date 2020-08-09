def check_if_n_and_double_exist(arr):
    for i in arr:
        if i == 0:
            return arr.count(0) == len(arr)
        if i / 2 in arr or i * 2 in arr:
            return True
    return False