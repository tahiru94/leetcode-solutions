def move_zeros(nums):
    count = 0
    while True:
        try:
            nums.remove(0)
            count += 1
        except:
            break
    if count > 0:
        nums.extend([0] * count)