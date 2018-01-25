#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001


a = [int(input()) for i in range(10)]

a.sort(reverse=True)
for i in range(3): 
    print(a[i])
