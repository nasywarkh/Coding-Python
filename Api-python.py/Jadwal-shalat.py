import requests
import json
from datetime import date

today = date.today()

def get_city_id(city):
    url = f"https://api.myquran.com/v2/sholat/kota/cari/{city}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == True:
        return data["data"][0]["id"]
    else:
        return None

def get_prayer_times(city_id):
    url = f"https://api.myquran.com/v2/sholat/jadwal/{city_id}/{today}"
    response = requests.get(url)
    data = response.json()
    return data["data"]["jadwal"]
    
city = "bandung"
city_id = get_city_id(city)

if city_id:
    data = get_prayer_times(city_id)
    print(f"Jadwal Shalat untuk Kota {city.capitalize()}")
    for key in data.keys():
        print(f"{key} : {data[key]}")
else:
    print("Kota tidak ditemukan.")



