#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include "MAX30105.h"

#define ky 3
#define ma 4

// 16 CHARACTERS AND 2 LINE DYSPLAY
LiquidCrystal_I2C lcd(0x27,16,2);

// Button control pins
byte kyInput;
byte maxInput;


// KYDataTransmision auxiliary variables
long HR;
int miliseconds = 0;
int initial;
int control;
byte t;

// Both use data to Send
String dataToSend;


// MaxModule stuff
MAX30105 particleSensor;
uint32_t redBuffer;
uint32_t irBuffer;
int hrBuffer;
int sensorHR;
long milis;



void maxModuleSetUp(){
  
  
  }


void KY039DataTransmition(){
  Serial.println("START KY TRANSMITION");
  initial = millis();
   while((control-initial)< 30000){
     HR=analogRead(1);
     miliseconds=millis();
     dataToSend="";
     dataToSend+=HR;
     dataToSend+=":";
     dataToSend+=miliseconds;
     Serial.println(dataToSend);
     control = millis();
    }
   Serial.println("End KY TRANSMITION");
   dataToSend = "";
  }






void lcdLoop(){
  lcd.clear();
  lcd.print("Heartrate: 1");
  lcd.setCursor(0,1);
  lcd.print("Oxygen: 2");
  }





void setup() {
  // put your setup code here, to run once:
  pinMode(ky,INPUT);
  pinMode(ma, INPUT);
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  dataToSend.reserve(100);


}

void loop() {
  // put your main code here, to run repeatedly:
  lcdLoop();
  kyInput = digitalRead(ky);
  maxInput = digitalRead(ma);
  if(kyInput == 1){
    KY039DataTransmition();
    }
  else if(maxInput == 1){
    Serial.println("enviar datos Max");
    }  

}
