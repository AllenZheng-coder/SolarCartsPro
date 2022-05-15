import RPi.GPIO as GPIO
import numpy as np
import time as t

GPIO.setmode(GPIO.BCM)  # 引脚设置为物理引脚模式

def read_temperture_humidity_data(DHT11_pin):
    '''
    This is a module to get DHT11's data
    Input DHT11.data pin's number(In BCM mode)
    Then it'll return a dictionary - {humidity,temperature}
    If the data has broken it'll return -1
    This module is unverify on raspberry
    By Duan-JunHan
    '''
    GPIO.setup(DHT11_pin, GPIO.OUT)   # 引脚设置为输出模式
    GPIO.output(DHT11_pin,GPIO.LOW)  
    t.sleep(0.02)                     # 发送20ms的低电平
    GPIO.output(DHT11_pin,GPIO.HIGH)  # 引脚转为高电平，起始信号发送完成
    
    GPIO.setup(DHT11_pin,GPIO.IN)     # 引脚设置成输入模式
    while GPIO.input(DHT11_pin) == GPIO.LOW:
        continue                      # 等待DHT11返回信号
    # DHT11会输入80us的低电平
    while GPIO.input(DHT11_pin) == GPIO.high:
        continue
    # 接着输出80us的高电平，应答信号接受完成，准备接受数据

    data_bits = 0     # 数据位数计数器
    data = []         # 存放二进制数据
    while(j < 40):    # DHT11的返回数据长40字节
        input_data = 0
        while GPIO.input(DHT11_pin) == GPIO.LOW:
            continue  
        # 数据每字节以50us的低电平为前导       
        while GPIO.input(DHT11_pin) == GPIO.HIGH:
            input_data += 1
            if(input_data > 25):
                break
        # 然后是26-28us的高电平（代表0），或者70us的高电平（代表1）
        if k < 8:
            data.append(0) # 26-28us时通常为6或7
        else:
            data.append(1) # 70us时通常为17或18
        j += 1 # 数据位数+1

    m = np.logspace(7,0,8,base=2,dtype=int) 
    # 创建一个[128,64,32,16,8,4,2,1]的数列
    data_arry = np.array(data)  # 将列表转为数组
    humidity = m.dot(data_arry[0:8])            # 计算湿度的整数部分
    humidity_float = m.dot(data_arry[8:16])     # 计算湿度的小数部分
    temperature = m.dot(data_arry[16:24])       # 计算温度的整数部分
    temperature_float = m.dot(data_arry[24:32]) # 计算温度的小数部分
    check_code = m.dot(data_arry[32:40])        # 计算校验码

    if (humidity + humidity_float + temperature + temperature_float) == check_code:
        return_dic = {'humidity':(humidity + humidity_float * (10 ** (-(len(str(humidity_float)))))),'temperature':(temperature + temperature_float * (10 ** (-(len(str(temperature_float))))))}
        return return_dic
        # 检查校验码，正确则输出
    else:
        return -1 # 否则输出-1