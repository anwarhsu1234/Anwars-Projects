This is only using ariduno so no need to do any python code. The way it works is that you need to use the Serial monitor to check if a tap has been detected. As you tap it should display "a tap has been detected. As you flip over the accelerometer to an downwards position and tap once more. You should also see the message "a tap has been detected."



Some flaws might include threshold values not working(this is because I set these settings to fit my needs so it might not work for someone else). Another flaw would be the transistion from upwards to downwards orientation. As you flip the breadboard over, the acclerometer might pick up a few false readings due to the instant change in accleometer z values. However, once you flip it to a staionary upsidedown position it should work. 