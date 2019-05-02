#include <SoftwareSerial.h>

SoftwareSerial ZERO(4, 7); // RX, TX

void software_Reset()
{
    asm volatile ("  jmp 0");  
} 

void setup() {
  Serial.begin(38400);
  while (!Serial)
  {
  }
  ZERO.begin(38400);
  while (!ZERO)
  {
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
