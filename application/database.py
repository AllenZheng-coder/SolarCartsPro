import pymysql

def signup(username, pass_word, phone, authority):
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="GoGreen@bd17z", database="gogreen", charset="utf-8")
        cur = conn.cursor()
        sql = """
        insert into user_info (username, pass_word, phone, authority) values ("{}","{}","{}","{}")
        """.format(username, pass_word, phone, authority)
        cur.execute(sql)
        conn.commit()
        return 0
    except:
        return -1

def login(username):
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="GoGreen@bd17z", database="gogreen", charset="utf-8")
        cur = conn.cursor()
        sql = """
        select pass_word, phone, authority from user_info where username="{}"
        """.format(username)
        return cur.fetchall()
    except:
        return -1

def write_in_weather(temperature, humidity, ultraviolet, precipitation, wind_speed,wind_direction,now_time):
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="GoGreen@bd17z", database="gogreen", charset="utf-8")
    cur = conn.cursor()
    sql = """
    insert into meteorology (temperature, humidity, ultraviolet, precipitation, wind_speed,wind_direction,now_time) values ("{}","{}","{}","{}","{}","{}","{}")
    """.format(temperature, humidity, ultraviolet, precipitation, wind_speed,wind_direction,now_time)
    cur.execute(sql)
    conn.commit()

def read_weather(now_time):
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="GoGreen@bd17z", database="gogreen", charset="utf-8")
        cur = conn.cursor()
        sql = """
        select temperature, humidity, ultraviolet, precipitation, wind_speed,wind_direction from meteorology where now_time="{}"
        """.format(now_time)
        cur.execute(sql)
        return cur.fetchall()
    except:
        return -1

# def setmod():
    
        