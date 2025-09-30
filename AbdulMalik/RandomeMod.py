import random
# for x in dir(random):
#     print(x)
# help(random.choice)
# help(random.randint)

l=["Apple","Orange","Mango","Pineapple"]
s=['$','&','*','(','^','#']
# print(random.choice(l))
# print(random.randint(1,25))
# print(random.choice(s))
password=random.choice(l)[random.randint(1,3):]+random.choice(s)+str(random.randint(1,100))+random.choice(l)[0]
print(password)