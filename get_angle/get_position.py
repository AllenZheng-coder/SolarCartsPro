import os 
import geoip2.database

os.system("curl ifconfig.me > IP.info")

with open("IP.info", "r", encoding="utf-8") as f:
    ip = f.read()

print("IP:", ip)

reader = geoip2.database.Reader("get_angle\geoip2_database\GeoLite2-City.mmdb")
data = reader.city(ip)
latitude = data.location.latitude
longitude = data.location.longitude
print("Latitude:", latitude)
print("Longitude:", longitude)