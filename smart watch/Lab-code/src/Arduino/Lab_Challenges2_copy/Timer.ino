void addTimer(){
  // add one to timer_seconds
  timer_seconds += 1;
  
  // print the time with printTime(//the integer to print)
  printTime(timer_seconds);  
}

void runTimer(){
  while(timer_seconds > 0){
    // minus one second from timer_second
    timer_seconds -= 1;
    // print the time with printTime(int)
    printTime(timer_seconds);
    // wait 1 second
    delay(1000);
  }
}

// ========= Timer Var ========= //

// ========== Timer Code ========= //
void runTimerOLED(){
 
  char message_buffer[4];

  while(timer_seconds > 0){
    timer_seconds--;
    String stringTime = String(timer_seconds);
    stringTime.toCharArray(message_buffer,4); //convert string to char buffer
    showMessage(message_buffer, 1, true);// show message_buffer with showMessage
    delay(20);
  }
}

// ========== Timer Code ========= //
void stateMachineTimer(){
  readADC();
  if (timer_state == 0){
    
    if(detectTap()){
      addTimerOLED();
      timer_state = 1;
    }
  }

  if (timer_state == 1){
   
   if (detectTap()){
      addTimerOLED();
      time_last_tap = millis();
      timer_state = 1;
   }
   if (millis() - time_last_tap > time_to_wait){
      timer_state = 2;
   }
  }
  
  if (timer_state == 2){
    runTimerOLED();
    timer_state = 3;
  }

  if (timer_state == 3){
    buzzMotor(255);
    if (detectTap()){
      buzzMotor(0);
      timer_state = 0;
    }
  }
  
  //Serial.println(timer_state);
  delay(100);
}
