def remove_duplicates(nums):
    temp = list(set(nums))
    nums.clear()
    nums.extend(temp)
    nums.sort()
    return len(nums)