import random
import math

# for i in range(5):
#     print(math.trunc(random.random()*1000))
# r=random.random()
# s1=random.getstate()
# print(r)
# print(r)
# print(r)
# print(r)
# random.setstate(s1)
# s2=random.getstate()
# r=random.random()
# random.setstate(s2)
# print(r)
# print(r)
# print(r)
# print(r)
# for i in range(5):
#     print(random.randint(25,50))
# print(random.randrange(0,100,1))
# print(random.randbytes(25))
# password=""
# for i in range(3):
#     password+=random.choice(['a','d','g','j','m','p'])
# password+=random.choice(['!','@','#','$','%','^','&','*'])
# password+=str(random.randint(1,100))
# print(password)
#
# tools=["chatGPT","Gemini","Grok","Claude","Deepseek","Copilot"]
# print(random.choice(tools))
a=random.randint(1,100)
c=0
score=100
while c<100:
    n=int(input("Enter your guess between 1 to 100: "))
    if n<0 or n>100:
        print("Wrong guess, please enter right guess")
        break
    else:
        if n==a:
            print("Your Right")
            print("Your Score = ",score)
            break
        elif n<a:
            print("Too Low")
            score-=10
        else:
            print("Too High")
            score-=10
        c+=1
else:
    print("You Lost!")
    print("Correct guess=",a)