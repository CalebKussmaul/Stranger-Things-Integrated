# Stranger things wall all in one!

In order to get around university internet restrictions, I origianlly set this up as 3 separate pieces, which you can find [here](https://github.com/CalebKussmaul/Stranger-Things-Wall)if you have similar needs. This version is reccomended as it is much simpler. 

#### All the hardware you will need (< $50):

1. Raspberry pi - any model should work, I'm using a B+
2. [Wifi dongle](https://www.amazon.com/gp/product/B003MTTJOY) if model does not have wifi chip
3. [5v Power supply](https://www.amazon.com/gp/product/B00MHV7576/) DO NOT POWER LEDs DIRECTLY FROM PI GPIO. CONNECT THEM BOTH TO THE POWER SUPPLY.
4. Breadboard and jumper wires 
5. [Level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) (Reccomended)
6. [WS2811 LEDs](https://www.amazon.com/gp/product/B01AG923GI/)
7. 3' x 4' posterboard, paint, command strips, clear tape

#### Instructions:

1. String wires on posterboard and paint letters corresponding to LEDs. There are 50 lights and 26 letters, so you will have to be somewhat creative. Use clear tape to point the LEDs to the letters
2. Install raspbian on pi
3. Connect pi and ws2811 LED strip to external 5v power source in parallel (see wiring below)
4. Connect LED data wire to the pi [GPIO 10](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png) (actual pin number 19, I know it's confusing)
5. Install [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x) (remember to disable sound card)
6. Open terminal
7. Enter "git clone 'https://github.com/CalebKussmaul/Stranger-Things-Integrated.git'"
8. if this fails Enter "sudo apt-get install git"
9. Enter "cd Stranger-Things-Integrated"
10. Enter "pip2 install -r requirements.txt"
11. Go into stranger.py and adjust character mapping to LEDs as necessary
12. Enter "python2 app.py"

You should now be up and running. Test it by entering a message in the terminal, or over the web by going to http://\[your pi's IP address\]:8080/stranger/

If you want to allow messages from the external internet, you will need to use your router port-forward incoming traffic to your external IP to the pi's internal IP.

Exit the program by entering "\exit" into the terminal

Note: technically the data wire takes 5v data, and the pi GPIO outputs on 3.3v. You may need to use [a level shifter](https://www.amazon.com/gp/product/B00XW2L39K/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) however it works fine without it for me.

#### Wiring:

![Wiring](wall%20with%20level%20shifter.png)

but you can probably get away with this:

![Wiring without level shifter](wall%20without%20level%20shifter.png)
