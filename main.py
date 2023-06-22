import time
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from rainbowio import colorwheel
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

from ctrlz import mode
from ctrlz import action
from ctrlz import screen

# Settings 
brightness = 0.05
current_mode = 1

def change_to_mode(i):
  # Modes
  current_mode = mode.modes[i]

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

change_to_mode(current_mode)

dial_pressed = False
dial_position = 0
dial_moving = False

while True:
  key_event = macropad.keys.events.get()
  if key_event:
    if key_event.pressed:
      # Action
      action = current_mode['actions'][key_event.key_number]
      if len(action['keys']) == 2:
        macropad.keyboard.send(action['keys'][0])
        time.sleep(0.4)
        macropad.keyboard.send(action['keys'][1])
      elif len(action['keys']) == 1:
        macropad.keyboard.send(action['keys'][0])

  #  Dial pressed
  if macropad.encoder_switch:
    dial_pressed = True
  
  # Dial released
  if dial_pressed and not macropad.encoder_switch:
    dial_pressed = False
    print("RELEASE")
    if brightness > 0.4:
      brightness = 0.05
    else:
      brightness = brightness + 0.05
    print(brightness)
    macropad.pixels.brightness = brightness
    macropad.pixels.show()

  # Dial turned
  if macropad.encoder != dial_position:
    dial_moving = True
    dial_moving_position = macropad.encoder

  # Mode up
  if dial_moving and (dial_moving_position - dial_position > 5):
    dial_position = macropad.encoder
    dial_moving = False
    if current_mode < len(mode.modes) - 1:
      current_mode = current_mode + 1
    else:
      current_mode = 0
    change_to_mode(current_mode)
  # Mode down
  elif dial_moving and (dial_moving_position - dial_position < -5):
    dial_position = macropad.encoder
    dial_moving = False
    if current_mode != 0:
      current_mode = current_mode - 1
    else:
      current_mode = len(mode.modes) - 1
    change_to_mode(current_mode)


