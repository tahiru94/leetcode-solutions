def sort_array_by_parity(A):
    evens = list(filter(lambda x: x % 2 == 0, A))
    odds = list(filter(lambda y: y % 2 != 0, A))
    A.clear()
    A.extend(evens + odds)
    return A