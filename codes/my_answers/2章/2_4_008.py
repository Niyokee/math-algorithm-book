N, S = map(int, input().split())

count = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if i + j <= S:
            count += 1
