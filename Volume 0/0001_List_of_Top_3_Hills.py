#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001
#高い順から三つ出力

a = [int(input()) for i in range(10)]

a.sort(reverse=True)
for i in range(3): 
    print(a[i])
