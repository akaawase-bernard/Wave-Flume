# Wave-Flume
A DIY wave generation project at UConn AirSea lab.
We have made a DIY Wave-Flume that uses a vertical piston design to make waves for demos.
This github page contains the arduino code to run the hardware, and the python code for measurements.
The design of the wave flume will be available as a CAD in the design folder.


# Using the Code
The first step in using the code would be to make sure you can run it. You should install Arduino IDE first to be able to run the code.
For us, we use the Arduino Uno, but other Arduinos should likely be able to run as well.
Use the same wiring that we use in the report to make the process smoother, as you do not want to mix up which pins connect to where.


Next, open the WaveFlume_controller.ino file in the Arduino IDE program.
You will see three different wave profiles already in the code.

```
WaveFlume_controller.ino
```

The wave 3 profile is already uncommented within the code to show what a running portion of code should look like.
If you want to switch between profiles, comment out the lines by using //, then delete the // in front of the code you want to use.
You can change how many seconds you would like the code to run by changing the duration value, which corresponds to seconds.


```
//Transfer Functions
int Time = (TIME - 0.0104) / (0.0052); // Adjusted travel time
int pulse = (displacement + 0.0325) / (0.041); // Number of pulses per travel
```

This transfer functions section shows the calculations to correct the distance(displacement) the plunger travels, and the time ajustment.
These functions are specialized for our case, you may have to remake these functions to get the distance and timing right if they are off.


The main section of code in the loop will oscillate the plunger up and down.
It will stop the loop after the duration you have selected is finished, and return the plunger to its original position.
The initial delay for setup line is commented out, as there was a bug affecting the first run once everything is reconnected. If bug persists, try uncommenting this line.

