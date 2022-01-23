def greatest_common_divisor(a: int, b: int) -> int:
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b
    return a if a > 1 else b
