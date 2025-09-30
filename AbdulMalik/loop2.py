'''
1: Read todays temp of MAlegaon city in a list after each hour
and count how many times the temp has crossed 25 deg
if temp corsses 25 more than 6 times, display its hot and humid
otherwise display normal

2: Read marks of 10 students in a tuple and find average marks, maximum
and minimum marks by using for loop and also find how many students got failed

3: Read details of a product in a list of dictionaries with kesy as
pid, pname, price, qty, now display only those products whose amount is
greater than 500

'''
temp=[22,20,38,31,29,30,30,40]
c=0
for i in temp:
    if i>35:
        c+=1
if c>=3:
    print("Its hot and humid",c)
else:
    print("Its normal",c)


marks=[20,65,74,95,29,37,49,52,30,25]
maximum=marks[0]
minimum=marks[0]
d=0
total=0
for item in marks:
    total+=item
    if maximum<item:
        maximum=item

    if minimum>item:
        minimum=item
    if item<35:
        d+=1

print(maximum)
print(minimum)
print(total/len(marks))
print(d)


n=int(input("Enter number of products: "))
products=[]
for i in range(n):
    myprod = dict()
    pid = int(input("Enter product id: "))
    pname = input("Enter product Name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter Qty: "))
    myprod["pid"] = pid
    myprod["pname"] = pname
    myprod["price"] = price
    myprod["qty"] = qty
    products.append(myprod)


products=[{'pid': 100, 'pname': 'mouse', 'price': 350.0, 'qty': 10}, {'pid': 101, 'pname': 'keyboard', 'price': 500.0, 'qty': 10}]
print(products)
for items in products:
    if items["price"]*items["qty"]>=5000:
        print("Product is under 5000")
    else:
        print("Product is under 8000")