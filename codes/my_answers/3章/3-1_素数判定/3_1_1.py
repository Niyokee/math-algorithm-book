# 計算量O(N)
def is_prime(n: int) -> bool:
    for i in (2, n+1):
        if n % i == 0:
            return False
    return True


n = int(input())


if is_prime(n):
    print('prime')
else:
    print('not prime')
