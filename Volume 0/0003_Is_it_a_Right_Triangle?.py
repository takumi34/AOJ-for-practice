#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0003

N = int(input())
for i in range(N):
    a,b,c =map(int, input().split() )
 
    a1 = a*a
    b1 = b*b
    c1 = c*c
    if a1 + b1 == c1 or b1 + c1 == a1 or c1 + a1 == b1:
        print("YES")
    else:
        print("NO")
