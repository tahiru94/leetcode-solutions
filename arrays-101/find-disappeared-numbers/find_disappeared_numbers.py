def find_disappeared_numbers(nums):
    if len(nums) == 0:
        return []
    full_nums = list(range(1, len(nums) + 1, 1))
    return list(set(full_nums) - set(nums))