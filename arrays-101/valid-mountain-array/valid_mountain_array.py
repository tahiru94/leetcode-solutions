def valid_mountain_array(A):
    if len(A) < 3 or sorted(A) == A or (len(A) == 3 and A[0] == A[-1]):
        return False
    else:
        max_A = max(A)
        max_A_index = A.index(max_A)

        if max_A_index != 0 and max_A_index != len(A):
            for i in range(0, max_A_index):
                if A[i] >= A[i + 1]:
                    return False
            for i in range(max_A_index, len(A) - 1):
                if A[i] <= A[i + 1]:
                    return False
        else:
            return False
        
        return True