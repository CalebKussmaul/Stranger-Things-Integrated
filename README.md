Stranger things wall, all in one!

All the hardware you will need (< $50):

1. Raspberry pi - any model should work, I'm using a B+
2. [Wifi dongle](https://www.amazon.com/gp/product/B003MTTJOY) if model does not have wifi chip
3. [5v Power supply](https://www.amazon.com/gp/product/B00MHV7576/) DO NOT POWER LEDs DIRECTLY FROM PI GPIO. CONNECT THEM BOTH TO THE POWER SUPPLY.
4. Breadboard and jumper wires 
5. [Level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) (Reccomended)
6. [WS2811 LEDs](https://www.amazon.com/gp/product/B01AG923GI/)
7. 3' x 4' posterboard, paint, command strips

Instructions:

1. Install raspbian on pi
2. Connect pi and ws2811 LED strip to external 5v power source in parallel (see wiring below)
3. Connect LED data wire to the pi [GPIO 10](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png) (actual pin number 19, I know it's confusing)
4. Install [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x) (remember to disable sound card)
5. Open terminal
6. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Integrated.git'"
7. if this fails Enter "sudo apt-get install git"
8. Enter "cd Stranger-Things-Integrated"
9. Enter "pip2 install -r requirements.txt"
10. Go into stranger.py and adjust character mapping to LEDs as necessary
11. Enter "python2 app.py" and it should start up

Note: technically the data wire takes 5v data, and the pi GPIO outputs on 3.3v. You may need to use [a level shifter](https://www.amazon.com/gp/product/B00XW2L39K/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) however it works fine without it for me.

![Wiring](wall%20with%20level%20shifter.png)

but you can probably get away with this:

![Wiring](wall%20without%20level%20shifter.png)
