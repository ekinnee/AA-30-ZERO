#include <SoftwareSerial.h>

SoftwareSerial ZERO(4, 7); // RX, TX

void software_Reset()
{
  asm volatile ("  jmp 0");  
} 

void setup() {
  ZERO.begin(38400); // init AA side UART
  ZERO.flush();
  Serial.begin(38400); // init PC side UART
  Serial.setTimeout(1000);
  Serial.flush();
  Serial.write("Init done.\r\n");
}

void loop() {
  if (ZERO.available()) {
    Serial.write(ZERO.read());
  }
  if (Serial.available()) {
    ZERO.write(Serial.read());
  }
}
