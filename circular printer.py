class Solution:
    def getTimes(string):
        out = 0
        prev_char = "A"
        for ch in string:
            gap = min((ord(ch) - ord(prev_char)) % 26, (-ord(ch) + ord(prev_char)) % 26)
            prev_char = ch
            out += gap
        return out


    print(getTimes("C"))

