def merge_sorted_array(nums1, m, nums2, n):
    temp_nums1 = nums1[:m]
    nums1.clear()
    nums1.extend(temp_nums1)
    nums1.extend(nums2)
    nums1.sort()