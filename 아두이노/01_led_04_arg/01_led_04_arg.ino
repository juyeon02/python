// 매개변수화
// 함수에는 매개변수를 사용하여 더 확정성 있는 함수를 선언할 수 있음

int leds[] = {12, 11, 10};
int count = 3;
int delayMS = 500;


void blinkAll(bool state) {
  for (int i = 0; i<count; i++){
    digitalWrite(leds[i], state ? HIGH : LOW);
    // state ? HIGH : LOW  ->  if문
    delay(delayMS);

  }
}

void setup() {
  for (int i = 0; i< count; i++){
    pinMode(leds[i], OUTPUT);
  }

  // put your setup code here, to run once:

}

void loop() {
  blinkAll(true);
  blinkAll(false);
  // put your main code here, to run repeatedly:

}
