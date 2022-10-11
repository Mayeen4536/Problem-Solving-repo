
a = [2,3,1,5,4,7,6]
n = 7


a.sort()
mid = int((n)/2)
print(mid)
print(a)
a[mid], a[n-1] = a[n-1], a[mid]

print(a)

st = mid + 1
ed = st + 1
while(a[st] <= a[ed]):
    a[st], a[ed] = a[ed], a[st]
    st = st + 1
    ed = ed + 1

print(a)
    

for i in range (n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i], end = ' ')
