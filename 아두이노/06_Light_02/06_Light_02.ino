void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);

  // 조도센서는 빛이 강하면 저항값이 작아짐 -> 전압(출력값)이 커짐
  // 조도센서는 빛이 약하면 저항값이 커짐 -> 전압(출력값)이 작아짐
  if (photoresistor > 500) {
    digitalWrite(2, HIGH);
  }

  else {
    digitalWrite(2, LOW);
  }
  // put your main code here, to run repeatedly:
}