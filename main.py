import time
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from rainbowio import colorwheel
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

from control_z import mode
from control_z import action
from control_z import screen

# Settings 
brightness = 0.05
DEFAULT_MODE = 'ride'
DIAL_CLICKS = 1
current_mode = None

def change_to_mode(mode_name):
  # Modes

  # Get screen for mode
  lines = screen.get_lines_for_mode(current_mode)
  display_lines = macropad.display_text()
  for i, line in enumerate(lines):
    display_lines[i].text = line
  display_lines.show()
  macropad.display.refresh()

  # Update key colors
  for i in range(12):
    macropad.pixels[i] = current_mode['actions'][i]['color']
  macropad.pixels.show()


# Init #######################
macropad = MacroPad()  # Set up MacroPad library and behavior
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False
macropad.pixels.brightness = brightness
macropad.keyboard.release_all()

current_mode = mode.get_mode_by_name(DEFAULT_MODE)
change_to_mode(current_mode)

dial_pressed = False
dial_position = 0
dial_new_position = None
new_mode = None

while True:
  key_event = macropad.keys.events.get()
  if key_event:
    if key_event.pressed:
      # Action
      #mode = mode.get_mode_by_index(current_mode)
      action = current_mode['actions'][key_event.key_number]
      if len(action['keys']) == 2:
        macropad.keyboard.send(action['keys'][0])
        time.sleep(0.4)
        macropad.keyboard.send(action['keys'][1])
      elif len(action['keys']) == 1:
        macropad.keyboard.send(action['keys'][0])

  # Dial turned
  if macropad.encoder != dial_position:
    new_mode_index = current_mode['index'] + (macropad.encoder - dial_position)
    if new_mode_index < 0:
      new_mode_index =  len(mode.modes) - 1
    elif new_mode_index > len(mode.modes) - 1:
      new_mode_index = 0
    new_mode = mode.get_mode_name_by_index(new_mode_index)
    current_mode = mode.get_mode_by_name(new_mode)
    change_to_mode(current_mode)
    dial_position = macropad.encoder

  #  Dial pressed
  if macropad.encoder_switch:
    dial_pressed = True
  
  # Dial released
  if dial_pressed and not macropad.encoder_switch:
    dial_pressed = False
    if brightness > 0.4:
      brightness = 0.05
    else:
      brightness = brightness + 0.05
    macropad.pixels.brightness = brightness
    macropad.pixels.show()
