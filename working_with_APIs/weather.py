import requests
import csv
import datetime
city=input("Enter City Name: ")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9420c5ba5ca896fa234e17236ae5ad38"
response=requests.get(url)
data=response.json()
print(data["weather"][0]["main"])
print(data["weather"][0]["description"])
print(data["main"]["temp"]-273.15)
print(data["main"]["temp_min"]-273.15)
print(data["main"]["temp_max"]-273.15)
print(data["main"]["humidity"])
print(data["wind"]["speed"])
time_zone=data["timezone"]
sunrise=data["sys"]["sunrise"]
sunset=data["sys"]["sunset"]
sunrise_time=datetime.datetime.utcfromtimestamp(sunrise+time_zone)
sunset_time=datetime.datetime.utcfromtimestamp(sunset+time_zone)

print(sunrise_time)
print(sunset_time)