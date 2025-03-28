#include <SPI.h>
#include <MFRC522.h>
#include <EEPROM.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance
int eepromAddress = 0; // Start EEPROM address

void setup() {
  Serial.begin(9600); // Initialize serial communications
  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522
  Serial.println("Scan an RFID card to read UID and save to EEPROM...");
}

void loop() {
  // Look for new cards
  if (!mfrc522.PICC_IsNewCardPresent() || !mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  // Read UID
  Serial.print("Card UID: ");
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();

  // Save UID to EEPROM
  saveUIDToEEPROM(eepromAddress, mfrc522.uid.uidByte, mfrc522.uid.size);

  // Increment EEPROM address for the next card
  eepromAddress += mfrc522.uid.size + 1; // +1 for length byte

  // Halt PICC
  mfrc522.PICC_HaltA();
  // Stop encryption on PCD
  mfrc522.PCD_StopCrypto1();

  // Wait before next scan
  delay(2000);
}

void saveUIDToEEPROM(int address, byte *uid, byte length) {
  EEPROM.write(address, length); // Write the length first
  for (int i = 0; i < length; i++) {
    EEPROM.write(address + 1 + i, uid[i]);
  }
  Serial.print("UID saved to EEPROM at address ");
  Serial.println(address);
}