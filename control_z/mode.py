import time
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

from control_z import action

def get_mode_by_name(name):
  for mode in modes:
    if mode['name'] == name:
      return mode
    
def get_mode_by_index(i):
  return modes[i]

def get_mode_name_by_index(i):
  return modes[i]['name']
    
def add_actions_to_mode(mode, action_names):
  for name in action_names:
    mode['actions'].append(action.get_action_by_name(name))

modes = []
modes.append({ 'name': 'ride', 'displayname': 'Ride', 'index': 0, 'actions': [] })
modes.append({ 'name': 'workout', 'displayname': 'Workout', 'index': 1, 'actions': [] })
modes.append({ 'name': 'race', 'displayname': 'Race', 'index': 2, 'actions': [] })
modes.append({ 'name': 'navigation', 'displayname': 'Navigation', 'index': 3,'actions': [] })
modes.append({ 'name': 'emotes', 'displayname': 'Emotes', 'index': 4, 'actions': [] })
modes.append({ 'name': 'camera', 'displayname': 'Camera', 'index': 5, 'actions': [] })

# TODO: Simplify this, just do it all inline above

ride = get_mode_by_name('ride')
add_actions_to_mode(ride, ['back', 'up', 'enter',
                           'left', 'down', 'right',
                           'pair', 'garage', 'screenshot',
                           'hud', 'powerup', 'graph'])

workout = get_mode_by_name('workout')
add_actions_to_mode(workout, ['back', 'up', 'enter',
                             'left', 'down', 'right',
                             'bias_up', 'skip', 'incline_up',
                             'bias_down', 'erg', 'incline_down'])

race = get_mode_by_name('race')
add_actions_to_mode(race, ['back', 'up', 'enter',
                             'left', 'down', 'right',
                             'elbow', 'rear', 'screenshot',
                             'powerup', 'powerup', 'powerup'])

navigation = get_mode_by_name('navigation')
add_actions_to_mode(navigation, ['pair', 'garage', 'blank',
                             'back', 'up', 'enter',
                             'left', 'enter', 'right',
                             'back', 'down', 'enter'])

emotes = get_mode_by_name('emotes')
add_actions_to_mode(emotes, ['elbow', 'wave', 'ride_on',
                             'hammer_time', 'nice', 'bring_it',
                             'toast', 'bell', 'blank',
                             'blank', 'blank', 'blank'])

camera = get_mode_by_name('camera')
add_actions_to_mode(camera, ['third', 'third_short', 'first',
                             'angled', 'chase', 'rear',
                             'sideline', 'helicopter', 'drone',
                             'blank', 'blank', 'blank'])

