import requests
import csv
from bs4 import BeautifulSoup

r=requests.get("https://www.bbc.com/sport/cricket/mens-australia-twenty20/table")
soup=BeautifulSoup(r.text,"html.parser")
table=soup.find("table")

th=table.find_all("th")[::2]
td=table.find_all("td")[::2]

all_headings=[h.get_text(strip=True) for h in th]

cleandata=[x.get_text(strip=True) for x in td]

rows=[]
for i in range(0,len(cleandata),len(all_headings)):
    rows.append(cleandata[i:i+len(all_headings)])

with open("Data.csv","w",newline="",encoding="utf-8") as fw:
    writer=csv.writer(fw)
    writer.writerow(all_headings)
    writer.writerows(rows)
print("All data saved!")
