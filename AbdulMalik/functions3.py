'''
3: Write a function to read names of fruits from the user in a tuple
and return the lengths of each fruit name in a list
'''

def lengthfruit(fruits):
    l=[]
    for p in fruits:
        l.append(len(p))
    return l
i=lengthfruit(("Apple","banana","orange","pineapple","cherry"))
print(i)