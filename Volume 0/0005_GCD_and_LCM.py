#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0005

import sys

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    return x * y// GCD(x, y)

for i in sys.stdin:
    a,b = map (int, i.split())
    print(GCD(a,b),LCM(a,b))
