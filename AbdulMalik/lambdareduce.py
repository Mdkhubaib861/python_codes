import functools
import operator

i=[54,96,81,34,94,86]
print(functools.reduce(lambda a,b:a if a>b else b,i))
print(functools.reduce(lambda a,b:a if a<b else b,i))
fruit=["Apple","Orange","Cherry","Mango","Avacado"]
print(functools.reduce(lambda a,b:a if len(a)>len(b) else b,fruit))
print(functools.reduce(lambda a,b:a if len(a)<len(b) else b,fruit))
print(functools.reduce(lambda a,b:a+b,list(range(0,int(input("Enter last number: "))))))
print(functools.reduce(operator.add,[45,86,34,79,26,74,93]))
print(functools.reduce(operator.mul,[45,74,93]))
print(functools.reduce(operator.sub,[45,74,93]))

