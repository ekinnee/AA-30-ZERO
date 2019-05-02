<<<<<<< HEAD
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
=======
#include <SoftwareSerial.h>

SoftwareSerial ZERO(4, 7); // RX, TX

void software_Reset()
{
    asm volatile ("  jmp 0");  
} 

void setup() {
    ZERO.begin(38400);
    Serial.begin(38400);
    while (!Serial)
    {}
    Serial.println("Ready");
}

void loop() {
    if (Serial.available() > 0)
    {
        ZERO.write(Serial.read());
    }
    if (ZERO.available() > 0)
    {
        Serial.write(ZERO.read());
    }
}
>>>>>>> 3b8f96c62c10c094f8f550a12de9f957d2514265
