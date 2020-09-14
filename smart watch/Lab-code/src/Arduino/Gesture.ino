
//TAP VARs
int negthreshZ = 2050;//determine the threshold you need
int threshZ = 2220;
int threshY = 0;
int threshX = 0;

// ===== Gesture Code  ========//
bool detectTap(){
  readADC();
  //read the ADC values. Note that the ADC values are global so you don’t need to define a local variable for them.
  
  bool tap_detected = false; // first set to false
  
  if( accelZ_Val < negthreshZ || accelZ_Val > threshZ ){
    tap_detected = true; //if the accel values meet the rule, set to true
  }
  return tap_detected;
}
