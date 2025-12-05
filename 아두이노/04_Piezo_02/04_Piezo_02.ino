const int melody[] = {
  // 도0 레1 미2 파3 솔4 라 시 도
  261.6, 293.7, 329.6, 349, 392, 440, 494, 523
};

const int PIEZO_PIN = 8;

void setup() {
  tone(PIEZO_PIN, melody[4], 500); delay(500);
  tone(PIEZO_PIN, melody[2], 500); delay(500);
  tone(PIEZO_PIN, melody[2], 500); delay(500);
  tone(PIEZO_PIN, melody[3], 500); delay(500);
  tone(PIEZO_PIN, melody[1], 500); delay(500);
  tone(PIEZO_PIN, melody[1], 500); delay(500);
  tone(PIEZO_PIN, melody[0], 500); delay(500);
  tone(PIEZO_PIN, melody[1], 500); delay(500);
  tone(PIEZO_PIN, melody[2], 500); delay(500);
  tone(PIEZO_PIN, melody[3], 500); delay(500);
  tone(PIEZO_PIN, melody[4], 500); delay(500);
  tone(PIEZO_PIN, melody[4], 500); delay(500);
  tone(PIEZO_PIN, melody[4], 500); delay(500);

}

void loop() {
}