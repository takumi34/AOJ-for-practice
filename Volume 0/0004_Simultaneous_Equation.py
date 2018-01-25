#問題　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0004
#連立１次方程式
import sys

for i in sys.stdin:
    a,b,c,d,e,f = map(float,i.split())
    g = a*e - b*d
    if(g != 0):　#連立方程式の解が一意に存在するという問題設定なのでなくても可
        x = (c*e-b*f)/g
        y = (a*f-c*d)/g  
        print("{:.3f} {:.3f}".format(x+0,y+0))
