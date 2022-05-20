import math as m
import datetime as dt
import pysolar as psl
import get_information

def sun_position(latitude,longitude,time_zone):
    """
    This is a module can calculate sun's position
    Please input two floats - latitude and longitude and one int - time_zone
    Output is a dictionary - {altitude_angle,azimuth_angle}
    The unit of measurement is degree(°) and hour(h)
    It uses a package - pysolar to give the answer precisely
    This is pysolar's website https://github.com/pingswept/pysolar/
    You can also use "pip install pysolar" to download it
    By Duan-JunHan
    """
    local_tz = dt.timezone(dt.timedelta(hours=time_zone))
    date = dt.datetime.now(tz=local_tz)
    print(date)
    altitude_angle = psl.solar.get_altitude(latitude, longitude, date)
    azimuth_angle = psl.solar.get_azimuth(latitude, longitude, date)
    return_dic = {'altitude_angle':altitude_angle,'azimuth_angle':azimuth_angle}
    return return_dic

def main():
    print("Auto following System Settings: ")
    while True:
        flag = input("Do you want to use the default setting[Y/N] ->")
        if flag == "Y" or flag == "y":
            latitude = get_information.get_position()["latitude"]
            longitude = get_information.get_position()["longitude"]
            time_zone = get_information.get_timezone()
            angle = sun_position(latitude,longitude,time_zone)
            print("altitude angle: ",angle["altitude_angle"] )
            print("azimuth angle: ",angle["azimuth_angle"] )
            return 0
        elif flag == "N" or flag == "n":
            while True:
                latitude = input("Please input your latitude ->")
                longitude = input("Please input your longitude ->")
                time_zone = input("Please input your timezone ->")
                try:
                    angle = sun_position(latitude,longitude,time_zone)
                    break
                except:
                    print("Someting went wrong! Please try again!")

            print("altitude angle: ",angle["altitude_angle"] )
            print("azimuth angle: ",angle["azimuth_angle"] )
            return 1
        else:
            print("We don't have this choice! Please enter again!")
        print("Setting successfully!")

if __name__ == "__main__":
    main()