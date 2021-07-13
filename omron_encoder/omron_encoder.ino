/* Encoder Library - Basic Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 *
 * This example code is in the public domain.
 */

#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(115200);
}

long oldPosition  = -999;
long previous_milis = millis();
long interval = 10.0;
void loop() {
  long current_milis = millis();
  if(((current_milis - previous_milis)) >= interval){
    long newPosition = myEnc.read();
    Serial.println(newPosition - oldPosition);
    previous_milis = current_milis;
    oldPosition = newPosition;
  }
}
