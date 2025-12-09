#define GAS_A A0
#define GAS_D 8
#define LED 9 // led
#define PIEZO 11 //부저

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(PIEZO, OUTPUT);
  Serial.begin(9600);
  Serial.println("히터 가열");
  delay(1000);

}

void loop() {
  digitalWrite(PIEZO, LOW); 
  digitalWrite(LED, LOW); 
  float sensorAvalue = analogRead(GAS_A);
  float sensorDvalue = digitalRead(GAS_D);

  Serial.print("아날로그 센서입력: ");
  Serial.print(sensorAvalue);

  if (sensorAvalue > 300 ) {
    Serial.print(" |연기감지! ");
    Serial.println("");
    digitalWrite(PIEZO, HIGH);
    digitalWrite(LED, HIGH); 
    delay(1000);

  }

  Serial.print("디지털 센서 입력: ");
  Serial.print(sensorDvalue);
  Serial.println("");

  delay(1000);
}
