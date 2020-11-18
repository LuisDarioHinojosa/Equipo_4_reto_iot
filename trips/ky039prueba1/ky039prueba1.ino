long HR;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  HR = analogRead(0);
  Serial.println(HR);
  delay(100);
}
