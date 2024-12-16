#include <Arduino.h>
#include <PCA9685.h>

#define LED_BUILTIN 2 

int num = 0;
int grow = 1;
uint16_t pwms[16]; // creates array for 16 servos 


PCA9685 pwmController(0x40);         // Library using B010101 (A5-A0) i2c address, and default Wire @400kHz

// put function declarations here:
int myFunction(int, int);

void setup() {
    // Initialize pin 13 as an output (typically the built-in LED).
    pinMode(LED_BUILTIN, OUTPUT);
	Serial.begin(115200);               // Begin Serial and Wire interfaces
    Wire.begin();

    pwmController.resetDevices();       // Resets all PCA9685 devices on i2c line

    pwmController.init();               // Initializes module using default totem-pole driver mode, and default phase balancer

    pwmController.setPWMFrequency(500); // Set PWM freq to 500Hz (default is 200Hz, supports 24Hz to 1526Hz)

    randomSeed(analogRead(0)); 
}

void loop() {
	if (grow)
	{
		num += 3;
		if (num >= 4096)
			grow = !grow;
	}
	else {
		num -= 3;
		if (num <= -4096)
			grow = !grow;	
	}
    	pwms[0] = num;
    	pwmController.setChannelsPWM(0, 16, pwms);
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}