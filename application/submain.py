from time import sleep
import datetime
import get_information
while True:
    sleep(3)
    weather = get_information.get_weather()
    with open(r"application\weather.csv", "a", encoding="gb2312") as f:
        f.write("\n{},{},{},{},{},{}".format(str(datetime.datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')),str(weather["weather"]),str(weather["temperature"]),str(weather["humidity"]),str(weather["pressure"]), str(weather["wind"]), str(weather["warning"])))


# with open(r"application\weather.csv", "a", encoding="utf-8") as f:
#     f.write("ok")