#define water_pin A0

void setup(){
    pinMode(water_pin,INPUT);
    Serial.begin(9600);
}

void loop(){
    data = (analogRead(water_pin)) / 650 * 4;
    Serial.println(data);
}