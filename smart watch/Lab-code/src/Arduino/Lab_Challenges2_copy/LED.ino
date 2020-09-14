int red_led = 26;
int yellow_led = 27;
int blue_led = 13;

void setupLED()  { 
  //Code for pin setups
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void condition1(){ 
  //Code for Condition 1
  //1HZ for built in LED
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}

void condition2(){ 
  //Code for Condition 2
  //10HZ for built in LED
  digitalWrite(LED_BUILTIN, HIGH);
  delay(50);
  digitalWrite(LED_BUILTIN, LOW);
  delay(50);
}

void condition3(){ 
  //Code for Condition 3
  //50 Hz for built in LED
  digitalWrite(LED_BUILTIN, HIGH);
  delay(10);
  digitalWrite(LED_BUILTIN, LOW);
  delay(10);
}

void condition4(){ 
  //Code for Condition 4
  //1s/100ms for RED LED 
  digitalWrite(red_led, HIGH);
  delay(1000);
  digitalWrite(red_led, LOW);
  delay(100);
}

void condition5(){ 
  //Code for Condition 5
  //200ms/50ms for yellow LED
  digitalWrite(yellow_led, HIGH);
  delay(200);
  digitalWrite(yellow_led, LOW);
  delay(50);
}

void condition6(){ 
  //Code for Condition 6
  //20ms/10ms for blue led
  digitalWrite(blue_led, HIGH);
  delay(20);
  digitalWrite(blue_led, LOW);
  delay(10);
}
