import random

fruits = ["Apple","Banana","Cherry","Mango","Orange","Pineapple","Strawberry","Grapes","Watermelon","Papaya","Kiwi","Blueberry","Guava","Lychee","Peach"]

g=random.choice(fruits)
print(g)

c=0
while c<4:
    f=input("Enter guess fruit name: ")
    if g==f:
        print("You Won the game!")
        break
    else:
        if c==0:
            print(f"Hint 1: The fruit have {len(g)} characters")
        elif c==1:
            n=""
            for i in range(len(g)-1):
                n+="*"
            n+=g[-1]
            print(n)
        elif c==2:
            n=""
            n+=g[0]
            for i in range(1,len(g)):
                n+="*"
            print("Hint 3:"+n)
        else:
            print("All Attempts Lost!")
            print(f"The fruit name is {g}")
        c+=1