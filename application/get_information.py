import os
import time
import geoip2.database
import math
from decimal import Decimal

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

def get_round(alpha):
    # for n in range(1, 180):
    #     cos_angle = Decimal(((60-0.34*n)**2)/(2*35.4*(60-0.34*n))).quantize(Decimal("0.00001"), rounding = "ROUND_HALF_UP")
        
    #     print(math.degrees(math.acos(cos_angle)))
    angle = Decimal(70.8 * float(Decimal(math.cos(math.radians(alpha))).quantize(Decimal("0.00001"), rounding = "ROUND_HALF_UP"))).quantize(Decimal("0.01"), rounding = "ROUND_HALF_UP")
    return angle