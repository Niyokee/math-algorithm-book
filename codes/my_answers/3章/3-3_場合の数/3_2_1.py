n = int(input())
a = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                for m in range(l + 1, n):
                    if a[i] + a[j] + a[k] + a[l] + a[m] == 1000:
                        answer += 1

N = int(input())
A = list(map(int, input().split()))

# 答えを求める
a = 0
b = 0
c = 0
d = 0
for i in range(N):
    if A[i] == 100:
        a += 1
    if A[i] == 200:
        b += 1
    if A[i] == 300:
        c += 1
    if A[i] == 400:
        d += 1

# 出力
print(a * d + c * d)