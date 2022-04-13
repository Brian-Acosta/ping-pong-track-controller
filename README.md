# ping-pong-track-controller
 Feedback controls project for PID control of a second order system. 
 Originally developed by Brian Acosta as a labratory exercise for ESE 505 (Feedback Control), at the University of Pennsylvania.

 ## Camera Setup Instructions - Read carefully!
 Note - these instructions were adapted from the OpenMV Cam tutorial [here](https://docs.openmv.io/openmvcam/tutorial/hardware_setup.html). You may wish to consult this tutorial if you need more detailed instructions or tourbleshooting advice. 
 1. Download and install the [OpenMV IDE](https://openmv.io/pages/download) 
 2. Plug in the OpenMV Board using a micro-USB cable 
 3. On windows, you should get notifications about installing drivers. 
    
    *Wait for drivers to be installed and for the blue LED on the OpenMV board to start blinking before proceeding*. 

    On Mac/Linux, wait for the  OpenMV Cam’s USB flash drive file browser window to appear (you may need to click on it in file explorer), and then wait for the blue LED.
 4. Launch OpenMV IDE and click on the "connect" button in the lower left corner (this looks like 2 plugs conntected)

 5. Follow the prompts to update the OpenMV firmware if necessary

 6. Run the `hello_world.py` script to check the functionality of the OpenMV camera by licking the play button in the lower left. 

## Ping Pong Table Setup
 7. After confirming the functionality of the camera, set up the ping pong table as shown in the circuit diagram.

 8. Open `ping_pong_controller.py` in the OpenMV IDE and upload to the board
