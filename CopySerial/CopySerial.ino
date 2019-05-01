#include <SoftwareSerial.h>

SoftwareSerial ZERO(4, 7); // RX, TX

void software_Reset()
{
  asm volatile ("  jmp 0");  
} 

void setup() {
  ZERO.begin(38400);
  Serial.begin(38400);
  while(!Serial) {
    //wait for serial monitor to connect
  }
}

void loop() {
  if (Serial.available())
  {
    ZERO.write(Serial.read());
  }
  if (ZERO.available())
  {
    Serial.write(ZERO.read());
  }
}
