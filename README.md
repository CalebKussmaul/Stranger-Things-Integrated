# Stranger things wall all in one!

In order to get around university internet restrictions, I origianlly set this up as 3 independent pieces which you can find [here](https://github.com/CalebKussmaul/Stranger-Things-Wall) if you have similar needs. This version is reccomended as it is much simpler. 

#### All the hardware you will need (~$50):

1. Raspberry pi - any model should work. [Zero W](https://www.adafruit.com/product/3400) + [GPIO header & adapters](https://www.amazon.com/dp/B075K7MG3F/) + [NOOBs](https://www.amazon.com/dp/B017JKJEAU) will be cheapest.
2. [Wifi dongle](https://www.amazon.com/gp/product/B003MTTJOY) if the pi does not have wifi chip
3. [5v Power supply](https://www.amazon.com/gp/product/B00MHV7576/) - DO NOT POWER LEDs DIRECTLY FROM THE PI
4. Breadboard and jumper wires (male/male and male/female)
5. [Level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) (Reccomended, seems to work without it)
6. [WS2811 LEDs](https://www.amazon.com/gp/product/B01AG923GI/)
7. 3' x 4' posterboard, paint, command strips, clear tape

#### Instructions:

1. String wires on posterboard and paint letters corresponding to LEDs. Use clear tape to point the LEDs to the letters.
  - Note: I suggest putting the input connector on the 'z' end if you want to put the pi below the board. 
2. Install Raspberry Pi OS on pi
3. Connect pi and ws2811 LED strip to external 5v power source in parallel (see wiring below)
4. Connect LED data wire to the pi [GPIO 10](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png) (actual pin number 19, I know it's confusing)
5. Open terminal
6. Enable SPI: 
  - Enter `sudo raspi-config`
  - Navigate to `Interfacing Options` and hit enter
  - Navigate to `SPI` and hit enter
  - Confirm and exit `raspi-config`
7. Enter `git clone 'https://github.com/CalebKussmaul/Stranger-Things-Integrated.git'`
8. Enter `cd Stranger-Things-Integrated`
9. Enter `pip install -r requirements.txt` (and wait...)
10. Edit the `stranger.py` file and adjust character mapping to the LED indexes as necessary
11. Enter `python app.py`

You should now be up and running. Test it by entering a message in the terminal, or over the web by going to http://\[your pi's IP address\]:8080/stranger/

If you want to allow messages from the external internet, you will need to use your router to port-forward incoming traffic from your external IP to the pi's internal IP.

Note: technically the data wire takes 5v data, and the pi GPIO outputs on 3.3v. You may need to use [a level shifter](https://www.amazon.com/gp/product/B00XW2L39K/) however it seems to work fine without it.

#### Wiring:

![Wiring](https://i.imgur.com/Cjj0dxo.png)

but you can probably get away with this:

![Wiring without level shifter](https://i.imgur.com/Vnqq14C.png)
