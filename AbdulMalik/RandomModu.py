import random
# for x in dir(random):
#     print(x)
#
# l=[67,693,348,397,37,132,48,38,41,35,]
# for i in range(random.randint(2,10)):
#     random.shuffle(l)
#     print(l)
# print(random.choice(l))
emails = [
    "x9k3z2lm@dummy.net",
    "a7b8c9d0@fakemail.org",
    "qwerty88@mockdata.dev",
    "zxcvbn12@placeholder.io",
    "testuser01@testmail.com",
    "useralpha23@dummy.net",
    "randomx45@fakemail.org",
    "mockingjay77@mockdata.dev",
    "ghostmail99@placeholder.io",
    "fakedata11@testmail.com",
    "dummyuser33@dummy.net",
    "placeholderx@fakemail.org",
    "junkmail007@mockdata.dev",
    "noreply22@placeholder.io",
    "tempuser66@testmail.com",
    "trialmail44@dummy.net",
    "samplex88@fakemail.org",
    "testcase55@mockdata.dev",
    "throwaway33@placeholder.io",
    "userbeta99@testmail.com",
    "anonmail77@dummy.net",
    "fakename12@fakemail.org",
    "mockuser21@mockdata.dev",
    "ghostuser88@placeholder.io",
    "tempaccount01@testmail.com"
]
for a in range(10):
    picked=[]
    for i in range(5):
        for j in range(random.randint(2,len(emails))):
            random.shuffle(emails)
        x=random.choice(emails)
        if x in picked:
            x=random.choice(emails)
        picked.append(x)
print(picked)

p=random.choices(emails,k=5)
print(p)