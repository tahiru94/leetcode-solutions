def find_max_consecutive_ones(nums: List[int]) -> int:
    split_ones = "".join([str(n) for n in nums]).split("0")
    length_of_ones = list(sorted([len(s) for s in split_ones]))

    return length_of_ones[-1]