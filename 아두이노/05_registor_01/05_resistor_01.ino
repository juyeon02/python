void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  int readValue = analogRead(A0);
  delay(500);
  Serial.println(readValue);
  // put your main code here, to run repeatedly:

}
