SHOW DATABASES;
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
    now_time datetime
)
CREATE TABLE settings
(
    runmod int,
    background text,
    chart text
    
)