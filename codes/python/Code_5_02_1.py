# 注意：以下のプログラムは N >= 1 で正しく動作します。
# N = 0 では答えは「1」となるので、また別の場合分けをする必要があります。

N = int(input())
if N % 4 == 1:
	print(2)
if N % 4 == 2:
	print(4)
if N % 4 == 3:
	print(8)
if N % 4 == 0:
	print(6)