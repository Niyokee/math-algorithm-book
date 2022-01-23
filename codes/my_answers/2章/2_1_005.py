from typing import List

A: List[int] = map(int, input().split())
print(sum(A) % 100)
