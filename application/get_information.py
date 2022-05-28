import os
import time
import geoip2.database
import math
from decimal import Decimal
import requests as req
import re as r
import get_information as gi

def get_position():
    with open("IP.info", "r", encoding="utf-8") as f:
        ip = f.read()
    
    response = req.get("http://ip-api.com/json/" + ip)
    info = eval(response.text)
    
    # reader = geoip2.database.Reader("application\geoip2_database\GeoLite2-City.mmdb")
    # data = reader.city(ip)
    # latitude = data.location.latitude
    # longitude = data.location.longitude
    return_dict = {"latitude":info["lat"], "longitude":info["lon"], "ip":info["query"]}
    print(return_dict)
    return return_dict

def get_timezone():
    now = time.time()
    now = time.localtime(now)
    timezone = time.strftime("%z", now)
    timezone = int(timezone[:3])
    return timezone

def get_round(alpha):
    # for n in range(1, 180):
    #     cos_angle = Decimal(((60-0.34*n)**2)/(2*35.4*(60-0.34*n))).quantize(Decimal("0.00001"), rounding = "ROUND_HALF_UP")
        
    #     print(math.degrees(math.acos(cos_angle)))
    angle = Decimal(70.8 * float(Decimal(math.cos(math.radians(alpha))).quantize(Decimal("0.00001"), rounding = "ROUND_HALF_UP"))).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
    return angle

def get_weather():
    response = req.get("https://wis.qq.com/weather/common?source=pc&weather_type=observe|forecast_24h|air&province=%E6%B2%B3%E5%8C%97%E7%9C%81&city=%E4%BF%9D%E5%AE%9A%E5%B8%82&county=%E8%8E%B2%E6%B1%A0%E5%8C%BA")
    txt = response.text
    # print(gi.get_position())
    with open('./html.txt','w',encoding='utf-8') as f:
        f.write(txt)
    temperature = r.search(r'"degree":"(.*)","humidity"',txt).group(1)
    humidity = r.search(r'"humidity":"(.*)","precipitation"',txt).group(1)
    pressure = r.search(r'"pressure":"(.*)","update_time"',txt).group(1)
    wind = r.search(r'"wind_power":"(.*)"}}',txt).group(1)
    weather = r.search(r'"weather":"(.*)","weather_code"',txt).group(1)
    return_dic = {"temperature":temperature,"humidity":humidity,"pressure":pressure,"wind":wind,"weather":weather}
    response = req.get("https://devapi.qweather.com/v7/warning/now?key=f1707f8e841e45eab98716e992e3c3e4&location=" + str(gi.get_position()["longitude"]) + "," + str(gi.get_position()["latitude"]))
    text = response.text.replace("[","").replace("]","")
    try:
        warning = eval(text)["warning"]
        del warning["id"]
        del warning["sender"]
        del warning["type"]
        del warning["related"]
        return_dic["warning"] = warning
    except:
        return_dic["warning"] = {}
    return return_dic

get_position()