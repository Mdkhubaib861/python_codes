def order(pid,pname,price,qty=10):
    print(pid,pname)
    print(price,qty,price*qty)

order(121,"Mouse",630,15)
order(121,"Mouse",630,)

def nraisedp(n,p=0):
    r=1
    for i in range(p):
        r=r*n
    print(n," riased to ",p,"=",r)
    print(f"{n} raised to {p}={r}")


nraisedp(5,10)
nraisedp(10,5)
nraisedp(5)