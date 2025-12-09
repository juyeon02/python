# include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
#define GAS_A A0

#define LED_R 6  
#define LED_G 4
#define LED_B 5

#define TRIG 9 //초음파 쏘는 곳 (수신부)
#define ECHO 8 //송신 받는 곳 


#define switch1 11
#define PIEZO 3

DHT dht(DHTPIN, DHTTYPE);

float getDitance() { // 실수 값을 반환하는 함수를 만들 때
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;

  return distance; // 초음파센서가 측정한 거리 값을 받음
}

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("히터 가열");
  delay(1000);
  pinMode(GAS_A, INPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(PIEZO, OUTPUT);
  pinMode(switch1, INPUT_PULLUP);

}

void loop() {
  float sensorAvalue = analogRead(GAS_A);
  float distance = getDitance();
  float h = dht.readHumidity(); 
  float c = dht.readTemperature(); 
  int SW1 = digitalRead(switch1);
  Serial.print("아날로그 센서입력: ");
  Serial.print(sensorAvalue);
  Serial.println("습도: " + String(h) + "% | 섭씨 온도:  " + String(c));
  Serial.print(distance);
  Serial.println("cm");
  delay(10);



  if (sensorAvalue > 200 ) {
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_B, LOW);
    digitalWrite(LED_G, LOW);
    Serial.print(" |연기감지! ");
    Serial.println("");
  }
  else if (sensorAvalue > 30) {
    digitalWrite(LED_B, HIGH);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_R, LOW);

  }
  else {
    digitalWrite(LED_R, LOW);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, LOW);
  }
  

  while (distance < 5){
    digitalWrite(LED_R, HIGH);
    delay(100);
    digitalWrite(LED_R, LOW);
    delay(100);
    
    int SW1 = digitalRead(switch1);

    if(SW1 == LOW) {
    Serial.println("Switch 눌림");
    digitalWrite(PIEZO, HIGH); 
    }

    else { digitalWrite(PIEZO, LOW); }

    distance = getDitance();
  }
  delay(500);
}