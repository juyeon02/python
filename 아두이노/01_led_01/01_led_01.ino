int Pin_r = 12;
int Pin_g = 11;
int Pin_b = 10;

void setup() {
  pinMode(Pin_r and, OUTPUT);
  pinMode(Pin_g, OUTPUT);
  pinMode(Pin_b, OUTPUT);
  
  // put your setup code here, to run once:
}

void loop() {
  digitalWrite(Pin_r, HIGH);
  digitalWrite(Pin_g, HIGH);
  digitalWrite(Pin_b, HIGH);
  delay(500);

  digitalWrite(Pin_r, LOW);
  digitalWrite(Pin_g, LOW);
  digitalWrite(Pin_b, LOW);
  delay(500);
  // put your main code here, to run repeatedly:

}
