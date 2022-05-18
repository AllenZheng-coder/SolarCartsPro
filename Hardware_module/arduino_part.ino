// 端口定义：
#define analogPin A0
#define digitalPin 2  

void setup() {
    Serial.begin(9600);
    pinMode(analogPin,INPUT);
    pinMode(digitalPin,OUTPUT);
}

void D2A(int analogPin)
{
    data = analogRead(analogPin);
    bool data_bin[10];
    for (int i = 0;i < 10;i++){
        data_bin[i] = (data % 2);
        data /= 2;
    }
    for(int i = 9;i >= 0;i--){
        Serial.print(data_bin[i]);
    }
    
    for(int i = 0; i < 10; ++i){
        if(data_bin[i])
            digitalWrite(i+2, HIGH);
        else
            digitalWrite(i+2, LOW);
        delay(2000)
    }
}

void loop() {
  int data = 265;
  Serial.println(data);
  bool data_bin[10];
  for (int i = 0;i < 10;i++){
    data_bin[i] = (data % 2);
    data /= 2;
  }
  for(int i = 9;i >= 0;i--){
    Serial.print(data_bin[i]);
  }
  
  for(int i = 0; i < 10; ++i){
    if(data_bin[i])
      digitalWrite(digitalPin, HIGH);
    else
      digitalWrite(digitalPin, LOW);
    
    Serial.delay(0.1)
  }
  Serial.print("\n");
}
