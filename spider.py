import requests as req
import re as r
import get_information as gi

def get_weather():
    response = req.get("https://wis.qq.com/weather/common?source=pc&weather_type=observe|forecast_24h|air&province=%E6%B2%B3%E5%8C%97%E7%9C%81&city=%E4%BF%9D%E5%AE%9A%E5%B8%82&county=%E8%8E%B2%E6%B1%A0%E5%8C%BA")
    txt = response.text
    print(gi.get_position())
    with open('./html.txt','w',encoding='utf-8') as f:
        f.write(txt)
    temperature = r.search(r'"degree":"(.*)","humidity"',txt).group(1)
    humidity = r.search(r'"humidity":"(.*)","precipitation"',txt).group(1)
    pressure = r.search(r'"pressure":"(.*)","update_time"',txt).group(1)
    wind = r.search(r'"wind_power":"(.*)"}}',txt).group(1)
    weather = r.search(r'"weather":"(.*)","weather_code"',txt).group(1)
    return_dic = {"temperature":temperature,"humidity":humidity,"pressure":pressure,"wind":wind,"weather":weather}
    response = req.get("https://devapi.qweather.com/v7/warning/now?f1707f8e841e45eab98716e992e3c3e4")
    return return_dic

if(__name__ == "__main__"):
    print(get_weather())