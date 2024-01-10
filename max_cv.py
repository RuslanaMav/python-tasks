n, m, s = map(int, input().split())
t1 = []
t2 = []

def add(y):
    for i in range(y):  
        a,b = map(str, input().split())
        t1.insert(i, a)
        t2.insert(i, b)

def d(x,y):
    for i in range(y):
        x.pop(-1)
 
def v1(x,y,z,e): #x - x[i], y - i, z - o, e - summ
    e = e + int (x)
    z = z + 1
    y = y + 1
    return e, z, y

def v2(x,y,z,e):# x - x[i-1], y - w, z - o,  e - summ
    e = e - int(x)
    z = z - 1
    y = 1
    return e, z, y

def summ(x, y, z, g):  
    o = 1
    i = 1
    u = 0
    w = 0
    summ = int(x[0])
    while w != 1:
        if i != z and u != g:
            if int(x[i]) <= int(y[u]):
                summ, o, i = v1(x[i], i, o, summ)
                if summ > s:
                    summ, o, w = v2(x[i-1], w, o, summ)
            else:
                summ,o,u = v1(y[u], u, o, summ)
                if summ>s:
                    summ, o, w = v2(y[u-1], w, o, summ)
        if w != 1:
            if i == z and u!= g:
                summ, o, u = v1(y[u], u, o, summ)
                if summ > s:
                    summ, o, w =v2(y[u - 1], w, o, summ)
                
            if u == g and i != z:
                summ, o, i = v1(x[i], i, o, summ)
                if summ>s:
                    summ, o, w = v2(x[i - 1], w, o, summ)
            if i == z and u == g:
                w = 1
    return (o)
    

if n > m:
    add(n)
else:
    add(m)

if n < m:
    k = m - n
    d(t1, k)
if m < n:
    f = n - m
    d(t2, f)  
    
r1 = summ(t1, t2, n, m)
r2 = summ(t2, t1, m, n) 
if r1 >= r2:
    print (r1) 
else:
    print (r2)
