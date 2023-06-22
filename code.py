import time
import board
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

#from ctrlz import page
#from ctrlz import button

# Init #######################
macropad = MacroPad()  # Set up MacroPad library and behavior
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False
macropad.pixels.brightness = 0.02
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
    lines.append("Ride Mode      1 of 5")
    lines.append("Esc     Up      Enter")
    lines.append("Left    Down    Right")
    lines.append("Dvcs    Grge    HUD")
    lines.append("SShot   PwrUp   Grph")
  return lines

ride_buttons = []

ride_buttons.append({ 'name': 'Back', 'shortname': 'Back', 'color': NEGATIVE, 'key': macropad.Keycode.ESCAPE })
ride_buttons.append({ 'name': 'Up', 'shortname': 'Up', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.UP_ARROW })
ride_buttons.append({ 'name': 'Enter', 'shortname': 'Enter', 'color': POSITIVE, 'key': macropad.Keycode.ENTER })

ride_buttons.append({ 'name': 'Left', 'shortname': 'Left', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.LEFT_ARROW })
ride_buttons.append({ 'name': 'Down', 'shortname': 'Down', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.DOWN_ARROW })
ride_buttons.append({ 'name': 'Right', 'shortname': 'Right', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.RIGHT_ARROW })

ride_buttons.append({ 'name': 'Devices', 'shortname': 'Dvcs', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.A })
ride_buttons.append( 'name': 'Garage', 'shortname': 'Grge', 'color': ZWIFT_ORANGE, 'key': macropad.Keycode.T })
ride_buttons.append({ 'name': 'HUD', 'shortname': 'HUD', 'color': ZWIFT_BLUE, 'key':  macropad.Keycode.H })

ride_buttons.append({ 'name': 'Screenshot', 'shortname': 'SShot', 'color': WHITE, 'key': macropad.Keycode.F10 })
ride_buttons.append({ 'name': 'Powerup', 'shortname': 'PwrUp', 'color': POWERUP, 'key': macropad.Keycode.SPACEBAR })
ride_buttons.append({ 'name': 'Graph', 'shortname': 'Grph', 'color': ZWIFT_BLUE, 'key': macropad.Keycode.G })

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