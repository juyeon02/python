# define TRIG 9 //초음파 쏘는 곳 (수신부)
#define ECHO 8 //송신 받는 곳 

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;
  Serial.print(distance);
  Serial.println("cm");
  delay(100);


  // put your main code here, to run repeatedly:

}
