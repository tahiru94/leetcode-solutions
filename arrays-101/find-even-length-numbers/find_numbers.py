def find_numbers(nums):
    num_lengths = [len(str(num)) for num in nums]
    even_lengths = [n for n in num_lengths if n % 2 == 0]
    
    return len(even_lengths)