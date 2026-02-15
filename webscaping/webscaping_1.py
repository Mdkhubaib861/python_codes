import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
r=requests.get(url)
print(r.status_code)
html_content=r.text

if r.status_code==200:
    print("you can scarp the data.")
    soup=BeautifulSoup(html_content,'html.parser')
    quotes=soup.find_all("div",class_="tags")
    for q in quotes:
        print(q.text)
        print("***************")
    
    authors=soup.find_all("a",class_="tag")
    for a in authors:
        print(a.text)

else:
    print("you can not scarp the data.")

