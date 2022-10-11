def gridChallenge(grid):
    # Write your code here
    for x in range(len(grid)):
        sorted(grid[x])
    
    for x in range(len(grid)):
        for y in range(len(grid)-1):
            if ord(grid[y][x]) < ord(grid[y + 1][x]):
                continue
            else:
                return str('NO')
             
    return str('YES')


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)

    print(result)
            