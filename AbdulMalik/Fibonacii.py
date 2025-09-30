def fib(n):
    if n==0 or n==1:
        return n
    else:
        f=fib(n-1)+fib(n-2)
    return f
for i in range(40):
    print(i,fib(i),sep="\t")