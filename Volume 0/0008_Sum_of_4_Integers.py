#問題 http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0008
import sys

for i in sys.stdin:
    n = int(i)
    s = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a + b + c + d == n:
                        s += 1
    print (s)
