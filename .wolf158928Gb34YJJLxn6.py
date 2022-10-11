def superDigit(n, k):
    # Write your code here
    s = n
    m = ''
    for _ in range(k):
        m = m + s

    # print(m)

    while len(m) > 1:
        l = list(m)
        l = [int(i) for i in l]
        m = str(sum(l))
        
    return m

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

# n = '131'
# k = 2

result = superDigit(n, k)
print(result)
