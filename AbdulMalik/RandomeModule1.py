import random

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

discounts = [50, 40, 30, 20, 10]
for a in range(1):
    picked = []
    for i in range(5):
        for j in range(random.randint(2, len(emails))):
            random.shuffle(emails)
        x = random.choice(emails)
        while x in picked:
            x = random.choice(emails)
        picked.append(x)
    print("Our Winners are!")
    for i in range(5):
        print(f"{picked[i]} gets {discounts[i]}% discount")