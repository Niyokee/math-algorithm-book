# 計算量O(√n)
def is_prime(n: int) -> bool:
    limit = int(n ** 0.5)
    for i in (2, limit + 1):
        if n % i == 0:
            return False
        return True


n = int(input())


if is_prime(n):
    print('prime')
else:
    print('not prime')
