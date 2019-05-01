#include <SoftwareSerial.h>
#include <avr/interrupt.h>

SoftwareSerial ZERO(4, 7); // RX, TX

const int rxpin = 0; // pin used to receive
const int txpin = 1; // pin used to send

void software_Reset()
{
  asm volatile ("  jmp 0");  
} 

void setup() {
<<<<<<< HEAD
  ZERO.begin(38400);
  Serial.begin(38400);
  while(!Serial) {
    //wait for serial monitor to connect
  }
=======
  sei();
  ZERO.begin(38400); // init AA side UART
  ZERO.flush();
  Serial.begin(38400);
  Serial.setTimeout(1000);

  while (!Serial) {
  }

>>>>>>> be680b8fc67bb1ea060447b1d7fb7fa789825265
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
