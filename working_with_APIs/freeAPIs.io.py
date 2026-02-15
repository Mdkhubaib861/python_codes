import requests

API = "https://api.alquran.cloud/v1"

print("Quran Text Program")

surah = input("Enter Surah number (1-114): ")

edition = "en.asad"

url = f"{API}/surah/{surah}/{edition}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nSurah:", data["data"]["englishName"])
    print("-" * 50)

    for ayah in data["data"]["ayahs"]:
        print(f"{ayah['numberInSurah']}. {ayah['text']}\n")
else:
    print("Error fetching data")
