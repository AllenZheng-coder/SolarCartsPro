import time as t
import smbus as sb   # 😅
import math as m


def read_word(address):
    high = bus.read_byte_data(address, address)    # 读取一个字节的数据
    low = bus.read_byte_data(address, address + 1)
    val = (high << 8) + low   # 计算数值
    return val

def read_I2C(address):
    res = read_word(address)
    if res >= 0x8000:
        return -((65535 - res) + 1)
    else:
        return res    # 将字节数据转为原码

def dist(a, b):   # 已知加速度求角度值
    return math.sqrt((a*a)+(b*b))

def getRotationX(x, y, z):
    radians = m.atan2(y, dist(x,z))
    return m.degrees(radians)

def getRotationY(x, y, z):
    radians = m.atan2(x, dist(y,z))
    return m.degrees(radians)


def read_accelerometer_data(Address):
    power_address = 0x6b # 电源控制寄存器地址
    bus = sb.SMBus(1)    # 初始化I2C
    bus.write_byte_data(Address, power_address, 0)  # 设置电源

    gyroX = read_I2C(0x43) / 131
    gyroY = read_I2C(0x45) / 131
    gyroZ = read_I2C(0x47) / 131   # 获取三轴旋转角度
    accelX = read_I2C(0x3b) / 16384   
    accelY = read_I2C(0x3d) / 16384
    accelZ = read_I2C(0x3f) / 16384   # 获取三轴加速度
    angleX = getRotationX(accelX/16384, accelY/16384, accelZ/16384)
    angleY = getRotationY(accelX/16384, accelY/16384, accelZ/16384) # 获取XY轴角度

    return_dic = {"gyroX":gyroX,"gyroY":gyroY,"gyroZ":gyroZ,"AccelX":accelX,"AccelY":accelY,"AccelZ":accelZ,"AngleX":angleX,"AngleY":angleY}
    return return_dic