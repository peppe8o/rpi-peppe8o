#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
#
#

import gpiozero
from time import sleep

# Class for traffic light module, using the GPIOZERO LEDBoard
class traffic_light:
  def __init__(self, red_LED, yellow_LED, green_LED):
    # NOTE: not well documented, however the LEDBoard seems to resort the LEDs order when assigned with a label.
    self.leds = gpiozero.LEDBoard(green = green_LED, red = red_LED, yellow = yellow_LED)

  def go(self):
    self.leds.value = (1, 0, 0) # Activates the GREEN LED and switches off all the other LEDs

  def stop(self, yellow_TIME = 3):
    self.leds.yellow.blink(on_time=0.8, off_time=0.8) # Blinks the YELLOW LED for "yellow_TIME" seconds with the following sleep statement
    sleep(yellow_TIME)
    self.leds.value = (0, 1, 0) # Activates the RED LED and switches off all the other LEDs

  def off(self):
    self.leds.off() # Switches off all the LEDS
