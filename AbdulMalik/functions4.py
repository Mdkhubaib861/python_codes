'''
4: Write a function to read a product detail in a dictionary from the user
 and return the dictionary values back to the function in a list.
'''

def prolist(d):
    return list(d.values())

l=prolist({"pid":121,"pname":"pen","price":20,"qty":20})
print(l)