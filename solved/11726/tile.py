n = int(input())
tiles = [1, 1, 3]

if n <= 2:
    print(tiles[n])
else:
    for i in range(n-2):
        tiles.append(tiles[-1] + 2*tiles[-2])
    print(tiles[-1] % 10007)