N, X, Y = map(int, input().split())

print(list(filter(lambda x: (x % X == 0) or (x % Y == 0), range(1, N + 1))))
