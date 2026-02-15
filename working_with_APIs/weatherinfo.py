from tkinter import *
import requests
import datetime
import csv
from tkinter import messagebox

w = Tk()
w.title("Weather & Namaz Time")
w.geometry("780x520")
w.resizable(False, False)

def getData():
    city = city_name.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=34f12fb726039d770b38e944994f51e1"
        data = requests.get(weather_url).json()

        if str(data.get("cod")) != "200":
            messagebox.showerror("Error", "Invalid city name")
            return

        weather.set(data["weather"][0]["main"])
        desc.set(data["weather"][0]["description"])
        temp.set(f"{round(data['main']['temp'] - 273.15, 2)} °C")
        humidity.set(f"{data['main']['humidity']} %")
        wind.set(f"{data['wind']['speed']} m/s")

        timezone = data["timezone"]
        sunrise = datetime.datetime.utcfromtimestamp(data["sys"]["sunrise"] + timezone)
        sunset = datetime.datetime.utcfromtimestamp(data["sys"]["sunset"] + timezone)

        sun_rise.set(sunrise.strftime("%H:%M:%S"))
        sun_set.set(sunset.strftime("%H:%M:%S"))

        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        namaz_url = f"https://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"
        namaz_data = requests.get(namaz_url).json()["data"]["timings"]

        fajr.set(namaz_data["Fajr"])
        dhuhr.set(namaz_data["Dhuhr"])
        asr.set(namaz_data["Asr"])
        maghrib.set(namaz_data["Maghrib"])
        isha.set(namaz_data["Isha"])

    except:
        messagebox.showerror("Error", "Unable to fetch data")

def saveCSV():
    if city_name.get() == "":
        messagebox.showerror("Error", "No data to save")
        return

    with open("weather_namaz_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            city_name.get(), weather.get(), desc.get(), temp.get(),
            humidity.get(), wind.get(), sun_rise.get(), sun_set.get(),
            fajr.get(), dhuhr.get(), asr.get(), maghrib.get(), isha.get()
        ])

    messagebox.showinfo("Success", "Data saved to CSV file")

def clearData():
    for v in vars_list:
        v.set("")

city_name = StringVar()
weather = StringVar()
desc = StringVar()
temp = StringVar()
humidity = StringVar()
wind = StringVar()
sun_rise = StringVar()
sun_set = StringVar()
fajr = StringVar()
dhuhr = StringVar()
asr = StringVar()
maghrib = StringVar()
isha = StringVar()

vars_list = [city_name, weather, desc, temp, humidity, wind, sun_rise, sun_set,
             fajr, dhuhr, asr, maghrib, isha]

Label(w, text="Weather & Namaz Time", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, pady=20)

Label(w, text="City Name:", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=15, pady=10, sticky="w")
Entry(w, textvariable=city_name, width=30).grid(row=1, column=1, columnspan=2, padx=10, pady=10)



Label(w, text="Weather:", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=weather, width=30, state="readonly").grid(row=4, column=1)

Label(w, text="Description:", font=("Arial", 12, "bold")).grid(row=4, column=2, padx=15, pady=6, sticky="w")
Entry(w, textvariable=desc, width=30, state="readonly").grid(row=4, column=3)

Label(w, text="Temperature:", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=temp, width=30, state="readonly").grid(row=5, column=1)

Label(w, text="Humidity:", font=("Arial", 12, "bold")).grid(row=5, column=2, padx=15, pady=6, sticky="w")
Entry(w, textvariable=humidity, width=30, state="readonly").grid(row=5, column=3)

Label(w, text="Wind:", font=("Arial", 12, "bold")).grid(row=6, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=wind, width=30, state="readonly").grid(row=6, column=1)

Label(w, text="Sunrise:", font=("Arial", 12, "bold")).grid(row=6, column=2, padx=15, pady=6, sticky="w")
Entry(w, textvariable=sun_rise, width=30, state="readonly").grid(row=6, column=3)

Label(w, text="Sunset:", font=("Arial", 12, "bold")).grid(row=7, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=sun_set, width=30, state="readonly").grid(row=7, column=1)

Label(w, text="Fajr:", font=("Arial", 12, "bold")).grid(row=8, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=fajr, width=30, state="readonly").grid(row=8, column=1)

Label(w, text="Dhuhr:", font=("Arial", 12, "bold")).grid(row=8, column=2, padx=15, pady=6, sticky="w")
Entry(w, textvariable=dhuhr, width=30, state="readonly").grid(row=8, column=3)

Label(w, text="Asr:", font=("Arial", 12, "bold")).grid(row=9, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=asr, width=30, state="readonly").grid(row=9, column=1)

Label(w, text="Maghrib:", font=("Arial", 12, "bold")).grid(row=9, column=2, padx=15, pady=6, sticky="w")
Entry(w, textvariable=maghrib, width=30, state="readonly").grid(row=9, column=3)

Label(w, text="Isha:", font=("Arial", 12, "bold")).grid(row=10, column=0, padx=15, pady=6, sticky="w")
Entry(w, textvariable=isha, width=30, state="readonly").grid(row=10, column=1)

Button(w, text="Get Data", command=getData, font=("Arial", 14, "bold")).grid(row=11, column=1, padx=10)
Button(w, text="Clear", command=clearData, font=("Arial", 14, "bold")).grid(row=11, column=2, padx=10)
Button(w, text="Save CSV", command=saveCSV, font=("Arial", 14, "bold")).grid(row=11, column=3, padx=10)

w.mainloop()