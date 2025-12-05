int LED_PIN = 3;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  analogWrite(LED_PIN, 255); //최대 출력 (DIGITALWRIGHT의 HIGH와 동일한 상태)
  delay(500);
  analogWrite(LED_PIN, 128); // 50%(2.5v) 출력
  delay(500);
  analogWrite(LED_PIN, 0); // 최소 출력 (DIGITALWRIGHT의 LOW와 동일한 상태)
  delay(500);

}
