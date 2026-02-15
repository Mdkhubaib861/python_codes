import requests
from bs4 import BeautifulSoup
import csv

url="https://quotes.toscrape.com/"
r=requests.get(url)
print(r.status_code)
html_content=r.text

if r.status_code==200:
    print("We can Scrap the data")
    soup=BeautifulSoup(html_content,'html.parser')
    quotes=soup.find_all("span",class_="text")

    for q in quotes:
        print(q.text)
        print("/*-/*-/*-/*-/*-/*-/")
    
    authors=soup.find_all("small",class_="author")
    for a in authors:
        print(a.text)

    with open("Duotes.csv","w",newline="",encoding="utf-8") as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(["Quotes","Author"])
        for q,a in zip(quotes,authors):
            csvWriter.writerow([q.text,a.text])
        f.close()
        print("All Data Stored into the file")


else:
    print("Cannot scrape the data")

