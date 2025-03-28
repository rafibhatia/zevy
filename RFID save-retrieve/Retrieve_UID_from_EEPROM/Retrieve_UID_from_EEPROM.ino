#include <EEPROM.h>

void setup() {
  Serial.begin(9600); // Initialize serial communications
  Serial.println("Retrieving UIDs from EEPROM...");
  printStoredUIDs();
}

void loop() {
  // Do nothing in loop
}

void printStoredUIDs() {
  int currentAddress = 0;
  while (true) {
    byte uidLength = EEPROM.read(currentAddress);
    if (uidLength == 0xFF || uidLength == 0x00) {
      break; // No more data or empty EEPROM
    }
    Serial.print("Stored UID at address ");
    Serial.print(currentAddress);
    Serial.print(": ");
    for (byte i = 0; i < uidLength; i++) {
      byte value = EEPROM.read(currentAddress + 1 + i);
      Serial.print(value < 0x10 ? " 0" : " ");
      Serial.print(value, HEX);
    }
    Serial.println();
    currentAddress += 1 + uidLength;
  }
}