void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);
  // put your main code here, to run repeatedly:

}
