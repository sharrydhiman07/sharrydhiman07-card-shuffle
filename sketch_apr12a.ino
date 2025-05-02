#include <DHT.h>

#define DHTPIN D4
#define DHTTYPE DHT11
#define LEDPIN D2    // You can choose any GPIO

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(LEDPIN, OUTPUT);  // Set LED pin as output
}

void loop() {
  float gas = analogRead(A0);         // MQ5
  float temp = dht.readTemperature(); // DHT22
  float hum  = dht.readHumidity();

  Serial.print(gas); Serial.print(",");
  Serial.print(temp); Serial.print(",");
  Serial.println(hum);

  // 🔴 AQI Alert using LED
  if (gas > 56.8) {
    digitalWrite(LEDPIN, HIGH);  // Turn ON LED
  } else {
    digitalWrite(LEDPIN, LOW);   // Turn OFF LED
  }

  delay(1000);
}
