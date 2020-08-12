def third_max(nums):
    unique_nums = list(set(nums))
    max_nums = []

    for _ in range(3):
        if len(unique_nums) > 0:
            current_max = max(unique_nums)
            max_nums.append(current_max)
            unique_nums.remove(current_max)
        else:
            break
    
    if len(max_nums) == 2:
        return max(max_nums)
    else:
        return sorted(max_nums)[0]