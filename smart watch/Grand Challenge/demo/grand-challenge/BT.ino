/*
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
int sampling_rate = 10; //sampling rate in Hz
unsigned long sampling_delay = calcSamplingDelay(sampling_rate); //microseconds between samples
unsigned long last_sample_time = 0; //microsecond of last sample

bool sending_data = false; //to send data?

// ==== Message VARs ====== //
char in_text[64];                // Character buffer
int in_text_index = 0;



void setupMessage(){
  SerialBT.begin("Anwar_FireBeetle"); //Defaults to 115200 Baud Rate
}

void printTime(int integer_to_print){
  // Serial print integer_to_print
  SerialBT.println(integer_to_print);
}

// ==== Message CODE ====== //
void receiveMessage(){
  if (SerialBT.available() > 0) { 
    
    char incomingChar = SerialBT.read();// read byte from serial
    if (incomingChar == '\n'){
      
      //show the in_text with show message
      showMessage(in_text, 1, true);
      checkMessage();
      
      //reset the in_text index back to 0
      in_text_index = 0;
      memset(in_text,0,20); // this will clear the in_text buffer
    }
    else{
      //assign in_text[index] to the incoming char
      in_text[in_text_index] = incomingChar;
      //increment the index
      in_text_index += 1;
    }
  }
}

void sendData(){
    if(sending_data){
        if(micros() - last_sample_time  > sampling_delay ){
            //update last_sample_time with current micros() 
            last_sample_time = micros(); 
            //read all ADC values
            readADC();
            //Serial print last_sample_time,x_val,y_val,z_val\n
            SerialBT.print(last_sample_time);
            SerialBT.print(",");
            SerialBT.print(accelX_Val);
            SerialBT.print(",");
            SerialBT.print(accelY_Val);
            SerialBT.print(",");
            SerialBT.println(accelZ_Val);
        }
    }
}

long calcSamplingDelay(long sampling_rate){
    return (1000000/sampling_rate);//number of microseconds to wait between samples
}


void checkMessage(){
  String message = String(in_text); // converts in_text into a string
  // Check if message is “stop data” or “start data”.
  // set sending_data according to the message received
  //delay for 1 second after setting send_data to true.
  if (message == "start data"){
    sending_data = true;
    sendData();
    delay(1000);
  }
  else{
    sending_data = false;
  }
  
}*/
