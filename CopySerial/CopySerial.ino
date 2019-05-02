//Copyright (C) 2019 Erick Kinnee erick@kinnee.net

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
