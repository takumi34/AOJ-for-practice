#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002

import sys
 
for i in sys.stdin:
    a,b = map(int, i.split())
    c = len(str(a+b))
    print(c)
