#define analogPin A0
#define digitalPin 2  

void setup() {
  Serial.begin(9600);
  pinMode(analogPin,INPUT);
  pinMode(digitalPin,OUTPUT);
}

void loop() {
//  int data = analogRead(analogPin);
  int data = 265;
  Serial.println(data);
  bool data_bin[10];
  for (int i = 0;i < 10;i++){
    data_bin[i] = (data % 2);
    data /= 2;
//    Serial.print(data_bin[i]);
  }
  for(int i = 9;i >= 0;i--){
    Serial.print(data_bin[i]);
  }
  Serial.print("\n");
//  if(data >= 512){
//     digitalWrite(digitalPin,LOW);
//  }else{
//    digitalWrite(digitalPin,HIGH);
//  }
}
