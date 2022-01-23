n = int(input())
blue_values = list(map(int, input().split()))
red_values = list(map(int, input().split()))

blue = 0.0
red = 0.0

for i in range(n):
    blue += blue_values[i] / n
    red += red_values[i] / n

print("%.12f" %(blue + red))
