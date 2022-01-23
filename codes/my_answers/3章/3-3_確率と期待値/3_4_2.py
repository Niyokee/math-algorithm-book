N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

answer = 0.0

for i in range(N):
    answer += 1/P[i] * Q[i]

print("%.12f" % answer)
