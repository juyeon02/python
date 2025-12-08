void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT); // LED 조정
}

void loop() {
  int readValue = analogRead(A0);
  Serial.println(readValue);
  readValue = map(readValue, 0, 1023, 0, 255);
  // map() : 입력값(0~1023)을 출력값(0~255)으로 변환
  // map(맵핑하려는 값, 입력범위의 최솟값, 입력볌위의 최댓값, 출력범위의 최솟값, 출력범위의 최댓값);
  // readValue = readValue * 255 / 1023 ; 
  analogWrite(10, readValue);
  delay(500);

}
