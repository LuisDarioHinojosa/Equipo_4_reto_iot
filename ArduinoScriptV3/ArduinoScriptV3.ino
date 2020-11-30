#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include "MAX30105.h"
#define ky 3
#define ma 4
#define buzz 12

// WiFI
#include <SoftwareSerial.h>//wifi
SoftwareSerial ESPserial(0, 1); //Wifi RX | TX
char data[100];
String command;
String response;




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


//String ssid = "INFINITUME681_2.4";
//String pass = "3QtSv7HK1X";

void wifiSetUp(){
  command.reserve(300);
  response.reserve(200);
  ESPserial.begin(9600);
  Serial.println("Setting up client mode");
  sendCommand("AT+CWMODE=1\r\n", 1000); 
  sendCommand2("AT+CWJAP=\"INFINITUME681_2.4\",\"3QtSv7HK1X\"\r\n", 4000,1); 
  delay(20000);
  sendCommand2("AT+CIPSTART=\"UDP\",\"192.168.1.70\",1337\r\n", 2000, 1);
  delay(1000);
  }



void buzzah(){
  tone(buzz,350);
  delay(1000);
  noTone(buzz);
  }


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
  buzzah();
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
    //enviar por wifi
    dataToSend+=";\r\n";
    command="AT+CIPSEND=";
    command+=dataToSend.length();
    command+="\r\n";
    sendCommand(command, 50);
    sendData(50);
   
    }
    flag = "END KY TRANSMITION";
   Serial.println(flag);
   dataToSend = "";
   buzzah();
  }





void lcdLoop(){
  lcd.clear();
  lcd.print("Heartrate: 1");
  lcd.setCursor(0,1);
  lcd.print("Oxygen: 2");
  delay(50);
  }





void setup() {
  // put your setup code here, to run once:
  pinMode(ky,INPUT);
  pinMode(ma, INPUT);
  pinMode(buzz,OUTPUT);
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
  buzzah();
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

     
    //enviar por wifi
    dataToSend+=";\r\n";
    command="AT+CIPSEND=";
    command+=dataToSend.length();
    command+="\r\n";
    sendCommand(command, 50);
    sendData(50);
  }
  dataToSend = "";
  flag = "END MAX TRANSMITION";
  Serial.println(flag);
  buzzah();
  }


void countDown(){
  lcd.clear();
  int count = 5;
  while(count > 0){
    dataToSend = "Measuring in ";
    dataToSend += count;
    lcd.print(dataToSend);
    delay(1000);
    count -=1;
    lcd.clear();
    }
  }


void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Waiting...");
  lcdLoop();
  kyInput = digitalRead(ky);
  maxInput = digitalRead(ma);
  if(kyInput == 1){
    countDown();
    KY039DataTransmition();
    }
  else if(maxInput == 1){
    countDown();
    maxDataTransmition();
    }  

}











void sendData(const int timeout)
{
  while ( ESPserial.available() ) {
    Serial.write( ESPserial.read());
    delay(1000);
  }
  response = "";
  int dataSize = dataToSend.length();
  dataToSend.toCharArray(data,dataSize);
  ESPserial.write(data,dataSize); // 
  long int time = millis();
  while( (time+timeout) > millis())
  {
  while(ESPserial.available())
  {
  // The esp has data so display its output to the serial window
  char c = ESPserial.read(); // read the next character.
  response+=c;
  }
  }
  Serial.print(response);
  //return response;
}

void sendCommand(String command, const int timeout)
{
  while ( ESPserial.available() ) {
    Serial.write( ESPserial.read());
    delay(100);
  }
  response="";
  ESPserial.print(command); // send the read character to the wifi
  long int time = millis();
  while( (time+timeout) > millis())
  {
  while(ESPserial.available())
  {
  // The esp has data so display its output to the serial window
  char c = ESPserial.read(); // read the next character.
  response+=c;
  }
  }
  Serial.print(response);
  //return response;
} 
void sendCommand2(String command, const int timeout, int times)
{
  response="";
  ESPserial.print(command); // send the read character to the wifi
  int i=0;
  while(i<times){
    long int time = millis();
    while( (time+timeout) > millis())
    {
    while(ESPserial.available())
    {
    // The esp has data so display its output to the serial window
    char c = ESPserial.read(); // read the next character.
    response+=c;
    }
    }
    Serial.print(response);
    i+=1;
  }

  //return response;
} 
