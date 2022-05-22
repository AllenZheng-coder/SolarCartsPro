SHOW DATABASES;
DROP DATABASE gogreen;
CREATE DATABASE gogreen;
CREATE TABLE user_info
(
    username text,
    pass_word text,
    phone text,
    authority text
);
CREATE TABLE meteorology
(
    temperature float,
    humidity float,
    ultraviolet int,
    precipitation float,
    wind_speed int,
    wind_direction int,
    pressure float,
    now_time datetime
);
CREATE TABLE settings
(
    times int,
    background text,
    chart_kind text,
    chart_color text,
    bar_dir text,
    ip text,
    latitude float,
    longitude float 
);