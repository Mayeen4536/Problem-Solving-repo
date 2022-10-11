

import re

# n = int(input().strip())

# arr = []

# for _ in range(n):
#     arr.append(list(map(str, input().split())))

arr = [['A12'], ['B3C4']]



arr1 = []
for x in arr:
    for y in x:
        
        # print(arr[x][y])
        arr1.append(re.findall('(\d+|[A-Za-z]+)', y))


arr2 = []
for x in range(len(arr1)):
    arr2.append([])
    for y in range(len(arr1[x])):
        # print(arr1[x][y])
        if y % 2 != 0:
            
            l = int(arr1[x][y])
            
            for _ in range(l):
                arr2[x].append(arr1[x][y-1])
str = ''

for x in range(len(arr2)):
   print('CASE',x+1,':',str.join(arr2[x]))




# arr = [['A2'], ['B3C4']]
# dict = {}
# new = [][]
# for x in range(len(arr)):
#     for y in range(x):
#         s = arr[x][y]


                

# print(new)
