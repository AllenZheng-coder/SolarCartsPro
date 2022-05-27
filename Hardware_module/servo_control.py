import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def servo_control(servo_pin,target_angle):
    '''
    This is a module to control servo TD7015MG
    Input servo's pin and target angle
    It'll control servo automatically
    If servo can't reach target it'll return -1
    This module is unverify on raspberry
    By Duan-JunHan
    '''
    PWMFrep = 50            # PWN信号频率设置为50Hz

    GPIO.setup(servo_pin,GPIO.OUT)       # 舵机信号脚设置为输出模式
    Pwm = GPIO.PWM(servo_pin,PWMFrep)    # 在舵机信号脚创建PWM对象
    Pwm.start(0)           # 启动PWM对象

    if(target_angle < 0 or target_angle > 180):
        return -1
    else:
        duty = (1 / 18) * target_angle + 2.5   # 角度转为占空比
        Pwm.ChangeDutyCycle(duty)        # 改变舵机角度
    
    Pwm.stop()             # 关闭PWM对象
    GPIO.cleanup()         # 清除GPIO资源，否则会报错