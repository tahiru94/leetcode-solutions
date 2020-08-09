def remove_element(nums, val):
    temp = [n for n in nums if n != val]
    nums.clear()
    nums.extend(temp)
    return len(nums)