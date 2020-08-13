from math import ceil

def reverse_string(s):
    def recursive_reverse(s, i, o):
        if i < o:
            s[i], s[o] = s[o], s[i]
            recursive_reverse(s, i + 1, o - 1)
        else:
            return
    recursive_reverse(s, 0, len(s) - 1)