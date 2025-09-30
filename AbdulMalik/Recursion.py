def add(i):
    print("Hello",i)
    i+=1
    if i==20:
        exit(0)
    add(i)
add(0)