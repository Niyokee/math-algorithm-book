def greatest_common_divisor(a: int, b: int) -> int:
    answer: int = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer


