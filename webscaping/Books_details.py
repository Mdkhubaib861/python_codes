import requests
from bs4 import BeautifulSoup
import csv



r=requests.get("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")
soup=BeautifulSoup(r.text,'html.parser')


Link=[]

price=[]

stock=[]

images=[]

alt=[]

all_Titles=soup.select("h3 a",attrs="title")

all_prices=soup.select("p.price_color")


for l in all_Titles:
    Link.append(l.get_text())


for pr in all_prices:
    price.append(pr.text[2:])

stock_details=soup.find_all("p",class_="availability")
for s in stock_details:
    stock.append((s.text).strip())

all_images=soup.find_all("img")
for i in all_images:
    images.append(i.get("src"))
    alt.append(i.get("alt"))

with open("BOOKS_DETAILS.csv","w",newline="",encoding="utf-8") as b:
        csvWriter=csv.writer(b)
        csvWriter.writerow(["link","price","stock","images","alt"])
        for l,p,s,i,a in zip(Link,price,stock,images,alt):
            csvWriter.writerow([l,pr.text[2:],s.strip(),i,a])
        b.close()

   

print("\n /*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/BOOKS_TATALS/*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/ \n")
print(price)
print("\n /*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/BOOKS_PRICES/*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/ \n")
print(Link)
print("\n /*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/BOOKS_STOCK/*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/ \n")
print(stock)
print("\n /*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/BOOKS_IMAGES_URL/*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/ \n")
print(images)
print("\n /*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/BOOKS_ALT/*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*//*-/*-/*-/*-/*-/*-*/-*/ \n")
print(alt)

