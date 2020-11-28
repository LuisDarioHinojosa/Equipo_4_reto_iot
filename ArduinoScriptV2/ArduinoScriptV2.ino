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

// User Variables
byte id = 1;
bool change = false;
bool prev = false;


// KYDataTransmision auxiliary variables
long HR;
long miliseconds = 0;
int initial;
int control;
byte t;

// Both use data to Send
String dataToSend;


// MaxModule stuff
MAX30105 particleSensor;
uint32_t redBuffer;
uint32_t irBuffer;
//int hrBuffer;
//int sensorHR;
long milis;

String flag = "";




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

void sendIdSignal(){
  dataToSend = "UserId: ";
  dataToSend += id;
  Serial.println(dataToSend);
  }



void maxModuleSetUp(){
  //sensorHR=1;
  // Initialize sensor
  while (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    Serial.println(F("MAX30102 was not found. Please check wiring/power."));
  }
  byte ledBrightness = 60; //Options: 0=Off to 255=50mA
  byte sampleAverage = 4; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  byte sampleRate = 100; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384
  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings
  
  }


void KY039DataTransmition(){
  flag = "START KY TRANSMITION";
  Serial.println(flag);
  initial = millis();
   while((control-initial)< 30000){
     HR=analogRead(1);
     miliseconds=millis();
     dataToSend="HR:";
     dataToSend+=HR;
     dataToSend+=";ML:";
     dataToSend+=miliseconds;
     Serial.println(dataToSend);
     control = millis();
    }
    flag = "END KY TRANSMITION";
   Serial.println(flag);
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
  flag.reserve(100);
  maxModuleSetUp();
  select();
  sendIdSignal();
}




void maxDataTransmition(){
  flag = "START MAX TRANSMITION";
  Serial.println(flag);
  int counter = 1;
  while(counter <=100 ){
     while (particleSensor.available() == false) //do we have new data?
     particleSensor.check();
     redBuffer = particleSensor.getRed();
     irBuffer = particleSensor.getIR();
     //hrBuffer = analogRead(sensorHR);
     //milis=millis();
     //dataToSend="HR:";
     //dataToSend+=hrBuffer;
     //dataToSend+=";ML:";
     //dataToSend+=milis;
     dataToSend ="RED:";
     dataToSend+=redBuffer;
     dataToSend+=";IR:";
     dataToSend+=irBuffer;
     Serial.println(dataToSend);
     counter += 1;
  }
  dataToSend = "";
  flag = "END MAX TRANSMITION";
  Serial.println(flag);
  }

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Waiting...");
  lcdLoop();
  kyInput = digitalRead(ky);
  maxInput = digitalRead(ma);
  if(kyInput == 1){
    KY039DataTransmition();
    }
  else if(maxInput == 1){
    maxDataTransmition();
    }  

}
