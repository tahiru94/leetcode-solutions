def height_checker(heights):
    sorted_heights = sorted(heights)
    result = [heights[i] != sorted_heights[i] for i in range(len(heights))]
    return result.count(True)