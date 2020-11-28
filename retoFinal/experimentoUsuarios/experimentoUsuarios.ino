#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#define ma 4
#define ky 3


// 16 CHARACTERS AND 2 LINE DYSPLAY
LiquidCrystal_I2C lcd(0x27,16,2);


byte id = 1;
bool change = false;
bool prev = false;
String dataToSend;


void select(){
  lcd.print("B1-> select");
  lcd.setCursor(0,1);
  lcd.print("B2-> confirm");
  delay(5000);
  lcd.clear();
  lcd.print("Select your ID:");
  while(digitalRead(ky) == 0){
    if(digitalRead(ma) == 1){
      change = !change;
      delay(500);
      }
    if(change != prev){
      prev = change;
      id += 1;
      if(id > 6){
        id = 1;
        }
      }
    lcd.setCursor(0,1);
    dataToSend = "IP: ";
    dataToSend += id;
    lcd.print(dataToSend);
    }
    lcd.clear();
    dataToSend = "Confirmed: ";
    dataToSend += id;
    lcd.print(dataToSend);
    delay(3000);
    lcd.clear();
  }



void setup() {
  // put your setup code here, to run once:
  lcd.begin();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  select();
}
