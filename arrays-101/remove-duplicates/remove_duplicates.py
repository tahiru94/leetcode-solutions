def remove_duplicates(nums):
    temp = sorted(list(set(nums)))
    nums.clear()
    nums.extend(temp)
    return len(nums)