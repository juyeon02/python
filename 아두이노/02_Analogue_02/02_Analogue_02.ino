int LED_PIN = 3;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  // 시리얼통신: 글자, 숫자, 데이터 값을 주고 받는 통신
  // Serial: 시리얼 통신을 담당하는 객체
  // .begin() : 시리얼 객체에 내장된 매서드
  // 시리얼 통신을 9600 속도로 시작해라
}

void loop() {
  for(int i = 0 ; i<255; i++){
  analogWrite(LED_PIN, i);
  delay(10);
  Serial.println(i);
  }
  // .println : 시리얼 모니터에 출력하는 함수
  // 통신상태를 확인하거나 디버깅용으로 사용

}
