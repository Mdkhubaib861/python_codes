import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    "https://en.wikipedia.org/wiki/List_of_footballers_with_500_or_more_goals",
    headers=headers
)

soup = BeautifulSoup(r.text, "html.parser")

# FIX: select the correct table
table = soup.find("table", class_="wikitable")

th = table.find_all("th")
td = table.find_all("td")

headings = [h.get_text(strip=True) for h in th]
cleandata = [x.get_text(strip=True) for x in td]

rows = []
for i in range(0, len(cleandata), len(headings)):
    rows.append(cleandata[i:i + len(headings)])

with open("Football.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(headings)
    writer.writerows(rows)

print("All data saved!")
