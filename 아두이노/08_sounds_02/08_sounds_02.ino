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
  digitalWrite(LED, HIGH);
  digitalWrite(PIEZO, HIGH);
  delay(1000);

  digitalWrite(TRIG, LOW);
  digitalWrite(LED, LOW);
  digitalWrite(PIEZO, LOW);
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;
  Serial.print(distance);
  Serial.println("cm");
  delay(100);

  if (ECHO < 12)



}
