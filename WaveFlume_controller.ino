
//In this code I have added the ENABLE pin and a counter.

// Define pin numbers
const int dirPin = 3;
const int stepPin = 4;
const int enablePin = 5; // New pin to control ENA+ on the driver

// ===========================================SELECT WAVE ===============================================
//Uncomment the wave profile you want to use


////Wave 1 (2 crests)
//int duration = 35;  // Running time in seconds
//int num_cycles = (duration - 0.0289) / (0.4815);  // Number of cycles that will run, dependent on duration set above
//int TIME = 1.5; // Time delay for pulses (in microseconds)  //1.5
//int displacement = 25; // Displacement value     //25
//int sleep = 5; // Delay between upward and downward travel (in milliseconds) //5

////int num_cycles = 100; // Number of cycles to run

//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

////Wave 2 (3 crests)
//int duration = 20;  // Running time in seconds
//int num_cycles = (duration + 0.0011) / (0.376);  // Number of cycles that will run, dependent on duration set above
//float TIME = 1.5; // Time delay for pulses (in microseconds)
//int displacement = 13; // Displacement value
//int sleep = 5; // Delay between upward and downward travel (in milliseconds)

////int num_cycles = 100; // Number of cycles to run

//=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

//////Wave 3 (5 crests) 
int duration = 30;  // Running time in seconds
int num_cycles = (duration - 0.0426) / (0.291);  // Number of cycles that will run, dependent on duration set above
int TIME = 1; //2--2Hz; // 1--4HzTime delay for pulses (in microseconds)
int displacement = 15; // Displacement value
int sleep = 5; // Delay between upward and downward travel (in milliseconds)

//////int num_cycles = 100; // Number of cycles to run

//==============================================================================================================


////////Wave 4 test (experimental)
//int duration = 20;  // Running time in seconds
//int num_cycles = (duration - 0.0289) / (0.4815);  // Number of cycles that will run, dependent on duration set above
//float TIME = 1; // Time delay for pulses (in microseconds)
//int displacement = 25; // Displacement value     
//int sleep = 5; // Delay between upward and downward travel (in milliseconds)
////int num_cycles = 100; // Number of cycles to run

//==============================================================================================================

//Transfer Functions
int Time = (TIME - 0.0104) / (0.0052); // Adjusted travel time
int pulse = (displacement + 0.0325) / (0.041); // Number of pulses per travel


void setup() {
  // Set pins as outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enablePin, OUTPUT); // Set enable pin as output
  
  // Enable the driver
  digitalWrite(enablePin, LOW); // LOW to enable the driver
  digitalWrite(dirPin, LOW);
  digitalWrite(stepPin, HIGH);
  //delay(25000); // Initial delay for setup... vital for the first run
}

void loop() {
  //initialize
  digitalWrite(dirPin, LOW); // Enable motor to move in a particular direction
  digitalWrite(stepPin, LOW);

  // Run the upward and downward motion for the specified number of cycles
  for (int i = 0; i < num_cycles; i++) {


    // Downward travel
    digitalWrite(dirPin, HIGH); // Set direction for downward travel
    for (int x = 0; x < pulse; x++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(Time);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(Time);
    }
   // delay(sleep); //temporary
   // Upward travel
    digitalWrite(dirPin, LOW); // Set direction for upward travel
    for (int x = 0; x < pulse; x++) {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(Time);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(Time);
    }

    delay(sleep); // Delay before downward travel
  }

  // Disable the driver after completing the cycles
  digitalWrite(enablePin, HIGH); // HIGH to disable the driver

  // Stop the loop after reaching the desired number of cycles
  while (true); // Keeps the program from looping indefinitely
}
