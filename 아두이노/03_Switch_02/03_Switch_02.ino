int switch1= 12; // 택트 스위치 1번과 연결된 디지털 핀 번호 
int switch2= 11; // 택트 스위치 2번과 연결된 디지털 핀 번호 
int ledRed = 4; // 택트 스위치 1번과 연결된 파란색 LED 핀 번호 
int ledGreen = 3; // 택트 스위치 2번과 연결된 빨간색 LED 핀 번호 

void setup() {
   Serial.begin(9600); // 9600 속도로 시리얼 통신을 시작
   pinMode(switch1, INPUT_PULLUP); // switch1번 핀을 인풋풀업으로 사용하겠다.
   pinMode(switch2, INPUT_PULLUP); 
   pinMode(ledGreen , OUTPUT); // 빨간색 디지털 핀으로 led를 켜기 위해 전력을 출력하겠다
   pinMode(ledRed , OUTPUT);
}

void loop() 
{
  int SW1 = digitalRead(switch1);
  // 인풋풀업 모드를 사용했기 때문에 기본적으로 1을 출력
  // 스위치가 눌리면 0을 출력
  int SW2 = digitalRead(switch2);

  digitalWrite(ledRed, LOW); 
  // led는 output 모드이기 때문에 기본 상태인 끈 상태는 low로 설정해야 함
  digitalWrite(ledGreen, LOW); 

  if(SW1 == LOW){ // 만약 sw1이 low라면? == 스위치를 눌렀을 때 ) 
    Serial.println("Switch : RED");
    digitalWrite(ledRed, HIGH); 
  }
  if(SW2 == LOW){
    Serial.println("Switch : GREEN");
    digitalWrite(ledGreen, HIGH); 
  }
  delay(100);
}