import math as m
import datetime as dt
import pysolar as psl


def sun_position(latitude,longitude,time_zone):
    """
    This is a module can calculate sun's position
    Please input two floats - latitude and longitude and one int - time_zone
    Output is two floats - altitude_angle and azimuth_angle
    The unit of measurement is degree(°) and hour(h)
    It uses a package - pysolar to give the answer precisely
    This is pysolar's website https://github.com/pingswept/pysolar/
    You can also use "pip install pysolar" to download it
    By Martin8521
    """
    local_tz = dt.timezone(dt.timedelta(hours=time_zone))
    date = dt.datetime.now(tz=local_tz)
    print(date)
    altitude_angle = psl.solar.get_altitude(latitude, longitude, date)
    azimuth_angle = psl.solar.get_azimuth(latitude, longitude, date)
    return altitude_angle,azimuth_angle

    #谁手算谁是大冤种[doge]
