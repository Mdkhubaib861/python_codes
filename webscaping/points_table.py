import requests
from bs4 import BeautifulSoup
import csv

p=requests.get("https://www.bbc.com/sport/cricket/mens-australia-twenty20/table")
print(p)
print(p)
soup=BeautifulSoup(p.text)
print(soup.prettify())
teams=soup.find_all("div",class_="ssrcss-ivmted-MobileWidthOnly e1sk6csp1")
all_teams=[]
for t in teams:
    all_teams.append(t.text)

all_played=[]
played=soup.find_all("div",class_="ssrcss-1vo7v3r-CellWrapper ef9ipf0")

for p in played:
    all_played.append(p.text)

t1=(list(map(float,all_played[:12])))[::2]
print(t1)
print("team_1")

t2=(list(map(float,all_played[12:24])))[::2]
print(t2)
print("team_2")

t3=(list(map(float,all_played[24:36])))[::2]
print(t3)
print("team_3")

t4=(list(map(float,all_played[36:48])))[::2]
print(t4)
print("team_4")

t5=(list(map(float,all_played[48:60])))[::2]
print(t5)
print("team_5")

t6=(list(map(float,all_played[60:72])))[::2]
print(t6)
print("team_6")

t7=(list(map(float,all_played[72:84])))[::2]
print(t7)
print("team_7")

t8=(list(map(float,all_played[84:96])))[::2]
print(t8)
print("team_8")



