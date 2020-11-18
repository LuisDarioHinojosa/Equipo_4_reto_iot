#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0X27,16,2);
long medition;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  medition = analogRead(0);
  lcd.clear();
  lcd.print("Oxigen: ");
  lcd.setCursor(9,0);
  lcd.print(medition);
  delay(500);
}
