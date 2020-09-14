#include <Wire.h>

// ========= Timer Var ========= //
int timer_seconds = 0;
unsigned long time_to_wait = 3000;

unsigned long time_last_tap = 0; //initiate the last tap time at 0

// ========= Timer Var ========= //
int timer_state = 0;


int HR_Data;






void setup() {
  // put your setup code here, to run once:
  setupMotor();
  setupADC();
  setupMessage();
  setupButton();
  setupLED();
  initDisplay();
  setupHR();



}


void Lab2_C1(){
  
  // buzz motor at full power for 1 second
  buzzMotor(255);
  delay(1000);
  
  // buzz motor at half power for 1 second
  buzzMotor(127);
  delay(1000);
  
  // don’t buzz for 1 second
  buzzMotor(0);
  delay(1000);
}


void Lab2_C2(){
  
  if(detectTap()){
    
    //add one second to the timer and show on OLED
    addTimerOLED();
    }
   
    
    delay(50);
}


void Lab2_C4(){

  if (detectTap()){
    addTimerOLED();
    time_last_tap = millis();
    
  }
  if (millis() - time_last_tap > time_to_wait){
    runTimerOLED();
  }
  printADC();
  delay(50);  
 
}

void Lab3(){
  receiveMessage(); //checks for serial message
  readHR();
  sendData(); //sends data via serial if suppose to
  
  
}

void Grand_challenge(){
readADC();
//printADC();
  if (detectTap()){
      Serial.println("A tap has been detected");
      delay(100);
  }
}
void loop() {
Grand_challenge();
}
    
    
  
