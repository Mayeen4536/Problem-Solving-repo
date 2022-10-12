def minimumBribes(q):
    # Write your code here
    n = 0
    
    for x in range(len(q)):
        m = 0
        for y in range(x, len(q)):
            l = 0
            print(q[x],q[y])
            if q[x] > q[y]:
                print(q[x], q[y])
                l += 1
                m += 1
                print(l)
                print(m)

                if m > 2:
                    print("Too Chaotic")
                    return

                    
                n += l
                print(n)
                
            # if q[x] > x+1:
            #     l = q[x] - (x+1)
            #     if l > 2:
            #         print('Too chaotic')
            #         return
            #     n+=l
    print(n)


    # def minimumBribes(q):
    # count = 0

    # for i in range(2):
    #     for j in range(len(q) - 1, 0, -1):
    #         if q[j] < q[j-1]:
    #             q[j], q[j-1] = q[j-1], q[j]
    #             count += 1

    # if q == sorted(q):
    #     print(count)
    # else:
    #     print('Too chaotic')



a = [2,5,1,3,4]
minimumBribes(a)
