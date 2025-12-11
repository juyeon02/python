const int PANEL_PIN = A0; // 태양광 패널 입력
const int SW_PIN = 2; // 판매버튼
long energy = 0; // 가상 에너지 저장소

const long SELL_UNIT = 100; // 100단위 판매
const int MAX_CHARGE_RATE = 50; // 전압이 5v 50씩 적립

void setup() {
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);

}


void loop() {
  // 태양광 패널 전압 읽기(0~5v)
  int raw = analogRead(PANEL_PIN);
  float voltage = (raw * 5.0) / 1023.0 ;

  // 전압 기반 충전 공식
  // gain = (전압비율) x (최대충전량)
  int gain = (voltage / 5.0) * MAX_CHARGE_RATE;


  if (gain > 0){ //충전된 전압을 energy라는 가상 저장소에 더함
    energy += gain;
  }

  bool prev = HIGH;
  bool curr = digitalRead(SW_PIN); 

  if ( prev == HIGH && curr == LOW){
    Serial.println("판매 요청");

    if(energy >= SELL_UNIT) {
      energy -= SELL_UNIT;
      Serial.print("판매 성공 | 판매량: " + String(SELL_UNIT) + "남은 에너지: " + String(energy));
    } else{
      Serial.println("판매 실패");
      Serial.println("저장된 에너지가 부족합니다");
      Serial.println("현재 에너지 : " + String(energy));
    }

    //현재 상태 출력
    Serial.print("전압: ");
    Serial.print(String(voltage));
    Serial.print("V | 전력량: +");
    Serial.print(String(gain));
    Serial.print("|현재 누적 에너지: ");
    Serial.print(String(energy));
    Serial.println("");

    delay(1000);


  } 





}
