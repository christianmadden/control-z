import time
from digitalio import DigitalInOut, Direction
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

from ctrlz import action

def get_mode_by_name(name):
  for mode in modes:
    if mode['name'] == name:
      return mode
    
def add_actions_to_mode(mode, action_names):
  for name in action_names:
    mode['actions'].append(action.get_action_by_name(name))

modes = []
modes.append({ 'name': 'ride', 'displayname': 'Ride', 'page': '1', 'actions': [] })
modes.append({ 'name': 'workout', 'displayname': 'Workout', 'page': '2', 'actions': [] })
modes.append({ 'name': 'race', 'displayname': 'Race', 'page': '3', 'actions': [] })
modes.append({ 'name': 'navigation', 'displayname': 'Navigation', 'page': '4','actions': [] })
modes.append({ 'name': 'emotes', 'displayname': 'Emotes', 'page': '5', 'actions': [] })
modes.append({ 'name': 'camera', 'displayname': 'Camera', 'page': '6', 'actions': [] })

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
                             'blank', 'blank', 'blank',
                             'elbow', 'powerup', 'rear'])

navigation = get_mode_by_name('navigation')
add_actions_to_mode(navigation, ['back', 'up', 'enter',
                             'left', 'down', 'right',
                             'blank', 'blank', 'blank',
                             'blank', 'blank', 'blank'])

emotes = get_mode_by_name('emotes')
add_actions_to_mode(emotes, ['elbow', 'wave', 'ride_on',
                             'hammer_time', 'nice', 'bring_it',
                             'toast', 'bell', 'blank',
                             'blank', 'blank', 'blank'])

camera = get_mode_by_name('camera')
add_actions_to_mode(camera, ['third', 'third_short', 'first',
                             'angled', 'chase', 'rear',
                             'sideline', 'helicopter', 'blank',
                             'blank', 'blank', 'blank'])

