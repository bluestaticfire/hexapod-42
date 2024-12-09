#include <Arduino.h>

#define LED_BUILTIN 2 

// put function declarations here:
int myFunction(int, int);

void setup() {
    // Initialize pin 13 as an output (typically the built-in LED).
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH); // Turn the LED on.
    delay(1000);                     // Wait for 1 second.
    digitalWrite(LED_BUILTIN, LOW);  // Turn the LED off.
    delay(1000);                     // Wait for 1 second.
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}