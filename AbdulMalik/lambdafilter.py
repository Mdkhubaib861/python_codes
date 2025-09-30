i=[5,9,36,7,56,14,42,89,28,37]
print(list(filter(lambda a:a%2,i)))
product={"Mouse":500,"Keyboard":1000,"Camera":2500,"Monitor":5000}
print(list(filter(lambda a:a>500,list(product.values()))))
marks=[26,35,89,78,59,85,94,93,71,85]
print(list(filter(lambda a:a>35 and a<100,marks)))
fruit=["Apple","Orange","Cherry","Mango","Avacado"]
print(list(filter(lambda a:a.startswith('A'),fruit)))
print(list(filter(lambda a:len(a)>5,fruit)))