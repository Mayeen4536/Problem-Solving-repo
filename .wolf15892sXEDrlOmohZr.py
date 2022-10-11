def superDigit(n, k):
    # Write your code here
    s = n
    for _ in range(k-1):
        for x in range(len(n)):
            s = s + n[x]

    # print(s)
    
    while len(s) > 1:
        l = list(s)
        l = [int(i) for i in l]
        s = str(sum(l))
        
    return s

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

# n = '12'
# k = 2

result = superDigit(n, k)
print(r)
