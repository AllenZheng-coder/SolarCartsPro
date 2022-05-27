import requests as req
import re as r
import get_information as gi

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
    # print("https://devapi.qweather.com/v7/warning/now?f1707f8e841e45eab98716e992e3c3e4&location=" + str(gi.get_position()["latitude"]) + "," + str(gi.get_position()["longitude"]))
    response = req.get("https://devapi.qweather.com/v7/warning/now?key=f1707f8e841e45eab98716e992e3c3e4&location=" + str(gi.get_position()["longitude"]) + "," + str(gi.get_position()["latitude"]))
    text = response.text.replace("[","").replace("]","")
    # text = """{
    # "code": "200",
    # "updateTime": "2021-10-10T12:20+08:00",
    # "fxLink": "http://hfx.link/2ax5",
    # "warning": [
    #     {
    #     "id": "10101010020211009154607668935939",
    #     "sender": "北京市气象局",
    #     "pubTime": "2021-10-09T15:46+08:00",
    #     "title": "北京市气象台2021年10月09日15时40分发布大风蓝色预警信号",
    #     "startTime": "2021-10-09T15:40+08:00",
    #     "endTime": "2021-10-10T15:40+08:00",
    #     "status": "active",
    #     "level": "蓝色",
    #     "type": "11B06",
    #     "typeName": "大风",
    #     "text": "市气象台2021年10月9日15时40分发布大风蓝色预警信号：预计，9日22时至10日19时，本市大部分地区有4级左右偏北风，阵风6、7级，山区阵风可达8级左右，请注意防范。",
    #     "related": ""
    #     }
    # ],
    # "refer": {
    #     "sources": [
    #     "12379"
    #     ],
    #     "license": [
    #     "commercial license"
    #     ]
    # }
    # }""".replace("[","").replace("]","")
    # warning = r.search(r'"warning":\[(.*)\]').group(1)
    try:
        warning = eval(text)["warning"]
        # print(gi.get_position())
        # with open('./html.txt','w',encoding='utf-8') as f:
        #     f.write(txt)
        del warning["id"]
        del warning["sender"]
        del warning["type"]
        del warning["related"]
        return_dic["warning"] = warning
    except:
        return_dic["warning"] = {}
    return return_dic

if(__name__ == "__main__"):
    print(get_weather())