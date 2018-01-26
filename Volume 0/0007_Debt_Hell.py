#問題 http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0007

import math
N = int(input())
a = 0
b = 100000
while a < N:
    b = (math.ceil(b*1.05/1000))*1000 #1000円以下は端数切り上げ
    a += 1
print(b)
