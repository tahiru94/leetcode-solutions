from math import ceil

def reverse_string(s):
    count = 0
    for i in range((len(s) - 1), (ceil(len(s) / 2) - 1), (-1)):
        initial = s[count]
        final = s[i]
        s[count] = final
        s[i] = initial
        count += 1