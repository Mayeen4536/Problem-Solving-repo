def caesarCipher(s, k):
    # Write your code here
    # a = []
    string = list(s)
    print(string)
    addNum = k

    length = len(string)
    for i in range(length):
        if ord(string[i]) <= ord("Z") and ord(string[i]) >= ord("A"):
            asciiCode = ord(string[i]) + addNum
            while asciiCode > ord("Z"):
                asciiCode = asciiCode - ord("Z") + ord("A") - 1
            string[i] = chr(asciiCode)
            print(string[i])
        elif ord(string[i]) <= ord("z") and ord(string[i]) >= ord("a"):
            asciiCode = ord(string[i]) + addNum
            while asciiCode > ord("z"):
                asciiCode = asciiCode - ord("z") + ord("a") - 1
            print(string)
            string[i] = chr(asciiCode)
            
        
    print("".join(string))
    









# n = int(input().strip())

# s = input()

s = 'middle-Outz'

# k = int(input().strip())
k = 2

caesarCipher(s, k)
