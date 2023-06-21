import time
import board
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

from zpad import button

# Init #######################
macropad = MacroPad()  # Set up MacroPad library and behavior
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False
macropad.pixels.brightness = 0.05
macropad.keyboard.release_all()

# Colors
ZWIFT_ORANGE = 0xFB6419
ZWIFT_BLUE = 0x5DC9DA
POSITIVE = 0x00FF00
NEGATIVE = 0xFF0000
POWERUP = 0x800080
WHITE = 0xFFFFFF

# Modes
mode = 'RIDE'

# 
def get_screen_for_mode(mode):
  lines = []
  if mode == 'RIDE':
    lines.append("Ride Mode            ")
    lines.append("View+   Menu:   More:")
    lines.append("SShot    HUD    Msgs:")
    lines.append("PwrUp   RdOn!   Emot:")
    lines.append("Left    UTurn   Right")
  return lines

ride_buttons = []
ride_buttons.append({ 'color': ZWIFT_BLUE, 'key': None })
ride_buttons.append({ 'color': ZWIFT_ORANGE, 'key': None })
ride_buttons.append({ 'color': NEGATIVE, 'key': None })

ride_buttons.append({ 'color': WHITE, 'key': macropad.Keycode.F10 })
ride_buttons.append({ 'color': POSITIVE, 'key': macropad.Keycode.H })
ride_buttons.append({ 'color': ZWIFT_BLUE, 'key': None })

ride_buttons.append({ 'color': POWERUP, 'key': macropad.Keycode.SPACEBAR })
ride_buttons.append({ 'color': ZWIFT_BLUE, 'key': macropad.Keycode.F3 })
ride_buttons.append({ 'color': ZWIFT_BLUE, 'key': None })

ride_buttons.append({ 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.LEFT_ARROW })
ride_buttons.append({ 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.DOWN_ARROW })
ride_buttons.append({ 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.RIGHT_ARROW })





# Update screen for mode
text_lines = macropad.display_text()
lines = get_screen_for_mode(mode)
for i, line in enumerate(lines):
  text_lines[i].text = line
text_lines.show()
macropad.display.refresh()

# Update button colors
for i in range(12):
  macropad.pixels[i] = ride_buttons[i]['color']
macropad.pixels.show()

while True:
  key_event = macropad.keys.events.get()
  if key_event:
    if key_event.pressed:
      print(key_event.key_number)
      macropad.keyboard.send(ride_buttons[key_event.key_number]['key'])

"""
WORKOUT
text_lines[0].text = "Workout Mode         "
text_lines[1].text = "View+   Menu:   More:"
text_lines[2].text = "SShot   HUD     Msgs:"
text_lines[3].text = "PwrUp   RdOn!   Selct"
text_lines[4].text = "FTP+    FTP-    Skip "
"""

"""
RACE
text_lines[0].text = "Race Mode            "
text_lines[1].text = "View+   Menu:   More:"
text_lines[2].text = "SShot    HUD    Msgs:"
text_lines[3].text = "Elbow   RdOn!   Emot:"
text_lines[4].text = "      Power-Up!      "
"""

"""
WORKOUT
macropad.pixels[0] = ZWIFT_BLUE
macropad.pixels[1] = ZWIFT_ORANGE
macropad.pixels[2] = NEGATIVE

macropad.pixels[3] = WHITE
macropad.pixels[4] = POSITIVE
macropad.pixels[5] = ZWIFT_BLUE

macropad.pixels[6] = POWERUP
macropad.pixels[7] = ZWIFT_BLUE
macropad.pixels[8] = ZWIFT_ORANGE

macropad.pixels[9] = POSITIVE
macropad.pixels[10] = NEGATIVE
macropad.pixels[11] = ZWIFT_ORANGE
"""

"""
RACE
macropad.pixels[0] = ZWIFT_BLUE
macropad.pixels[1] = ZWIFT_ORANGE
macropad.pixels[2] = NEGATIVE

macropad.pixels[3] = WHITE
macropad.pixels[4] = POSITIVE
macropad.pixels[5] = ZWIFT_BLUE

macropad.pixels[6] = ZWIFT_BLUE
macropad.pixels[7] = ZWIFT_BLUE
macropad.pixels[8] = ZWIFT_BLUE

macropad.pixels[9] = POWERUP
macropad.pixels[10] = POWERUP
macropad.pixels[11] = POWERUP
"""