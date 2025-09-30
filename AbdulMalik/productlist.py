'''
products=[]
n=int(input("Enter number of products: "))
for i in range(n):
    myprod=dict()
    pid=int(input("Enter product id: "))
    pname=input("Enter product name: ")
    category=input("Enter product category: ")
    price=float(input("Enter product price: "))
    qty=int(input("Enter qty: "))
    amount=qty*price
    myprod["pid"]=pid
    myprod["pname"]=pname
    myprod["category"]=category
    myprod["price"]=price
    myprod["qty"]=qty
    myprod["amount"]=amount
    products.append(myprod)
print(products)
'''

products=[{'pid': 1, 'pname': 'pens', 'category': 'stationary', 'price': 20.0, 'qty': 42, 'amount': 840.0},
{'pid': 2, 'pname': 'laptop', 'category': 'electronics', 'price': 54000.0, 'qty': 3, 'amount': 162000.0},
{'pid': 3, 'pname': 'cellphone', 'category': 'electronics', 'price': 23000.0, 'qty': 3, 'amount': 69000.0},
{'pid': 4, 'pname': 'notebook', 'category': 'stationary', 'price': 30.0, 'qty': 50, 'amount': 1500.0}]
print("All products: ")

for p in products:
    print(p)

print("1: For Total Amount:")
print("2: Products Amount>=25000:")
print("3: Products With stationary category:")
print("4: Products with category Electronics:")
o=int(input("Enter option: "))
if o==1:
    total_amount=0
    for p in products:
        total_amount+=p["amount"]
    print("Total Amount=",total_amount)
elif o==2:
    for p in products:
        if p["amount"]>=25000:
            print(p)
elif o==3:
    for p in products:
        if p["category"]=="stationary":
            print(p)
elif o==4:
    total_amount=0
    for p in products:
        if p["category"]=="electronics":
            total_amount+=p["amount"]
        print("Total Amount of electronics=",total_amount)
else:
    print("Invalid Option")