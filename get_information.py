import os 
import time
import geoip2.database

def get_position():
    os.system("curl ifconfig.me > IP.info")

    with open("IP.info", "r", encoding="utf-8") as f:
        ip = f.read()

    print("IP:", ip)

    reader = geoip2.database.Reader("application\geoip2_database\GeoLite2-City.mmdb")
    data = reader.city(ip)
    latitude = data.location.latitude
    longitude = data.location.longitude
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    return {"latitude":latitude, "longitude":longitude}

def get_timezone():
    now = time.time()
    now = time.localtime(now)
    timezone = time.strftime("%z", now)
    timezone = int(timezone[:3])
    return timezone
