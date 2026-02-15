import requests
import os
import time

print("Quran Audio Mini Program")
surah = input("Enter Surah number (1-114): ").strip()
edition = "ar.alafasy"
API = "https://api.alquran.cloud/v1"
url = f"{API}/surah/{surah}/{edition}"
response = requests.get(url, timeout=20)
data = response.json()
print("\nSurah:", data["data"]["englishName"])
print("Total verses:", data["data"]["numberOfAyahs"])
print("--------------------------------------")
base_dir = os.path.abspath("audio")
os.makedirs(base_dir, exist_ok=True)
for ayah in data["data"]["ayahs"]:
    ayah_no = ayah["numberInSurah"]
    audio_url = ayah["audio"]

    print("Downloading Ayah", ayah_no)
    filename = os.path.join(base_dir, f"ayah_{ayah_no}.mp3")
    audio_url = audio_url.replace("http://", "https://")

    r = requests.get(audio_url, stream=True, timeout=30)
    r.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    if not os.path.exists(filename) or os.path.getsize(filename) < 5000:
        print("Failed to download Ayah", ayah_no)
        continue

    print("Playing Ayah", ayah_no)
    os.startfile(filename)

    time.sleep(7)

print("Surah finished")
