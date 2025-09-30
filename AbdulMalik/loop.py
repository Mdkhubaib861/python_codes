'''
1: Display your name five times on screen
2: Display the numbers from 1 to 10
3: Display the numebrs from 1 to 100 with step size 11
4: Display all numebrs between 1 to 100 which are divisible by 5
5: Display all numebrs between 100 to 10 in decreasing order with step size 2

for c in range(5):
    print("Maaz :")

for i in range(1,11):
    print(i)

for a in range(1,101,11):
    print(a)

for w in range(5,101,5):
    print(w)

for d in range(100,10,-2):
print(d)
'''
n=int(input("Enter number of products: "))
products=[]
for i in range(n):
    myprod=dict()
    pid=int(input("Enter product id: "))
    pname=input("Enter product Name: ")
    price=float(input("Enter price: "))
    qty=int(input("Enter Qty: "))
    myprod["pid"]=pid
    myprod["pname"] = pname
    myprod["price"] = price
    myprod["qty"] = qty
    products.append(myprod)

products=[{'pid': 101, 'pname': 'Pen', 'price': 5.0, 'qty': 20}, {'pid': 102, 'pname': 'Pencil', 'price': 5.0, 'qty': 100}, {'pid': 103, 'pname': 'notebook', 'price': 25.0, 'qty': 50}]
# print(products)
for items in products:
    if items["price"]*items["qty"]>=500:
