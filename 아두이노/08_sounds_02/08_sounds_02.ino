# define TRIG 9 //초음파 쏘는 곳 (수신부)
#define ECHO 8 //송신 받는 곳 
#define LED 5 // led
#define PIEZO 3 //부저

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(PIEZO, OUTPUT);
}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(10);

  digitalWrite(TRIG, LOW);

  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;
  Serial.print(distance);
  Serial.println("cm");
  delay(10);

  if (distance < 12){
    digitalWrite(LED, HIGH);
    digitalWrite(PIEZO, HIGH);
    delay(100);
    digitalWrite(LED, LOW);
    digitalWrite(PIEZO, LOW);
    delay(10);

  }
  



}
