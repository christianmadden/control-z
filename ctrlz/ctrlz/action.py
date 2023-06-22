from adafruit_macropad import MacroPad

# Colors
ZWIFT_ORANGE = 0xFB6419
ZWIFT_BLUE = 0x5DC9DA
POSITIVE = 0x00FF00
NEGATIVE = 0xFF0000
WARN = 0xFFFF00
POWERUP = 0x800080
WHITE = 0xFFFFFF
DISABLED = 0x000000
 
actions = []

# Navigation
actions.append({ 'name': 'back', 'displayname': 'Back', 'color': NEGATIVE, 'keys': [MacroPad.Keycode.ESCAPE] })
actions.append({ 'name': 'enter', 'displayname': 'Enter', 'color': POSITIVE, 'keys': [MacroPad.Keycode.ENTER] })
actions.append({ 'name': 'up', 'displayname': 'Up', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.UP_ARROW] })
actions.append({ 'name': 'down', 'displayname': 'Down', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.DOWN_ARROW] })
actions.append({ 'name': 'left', 'displayname': 'Left', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.LEFT_ARROW] })
actions.append({ 'name': 'right', 'displayname': 'Right', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.RIGHT_ARROW] })

# Menus
actions.append({ 'name': 'pair', 'displayname': 'Pair', 'color': ZWIFT_ORANGE, 'keys': [MacroPad.Keycode.A] })
actions.append({ 'name': 'garage', 'displayname': 'Garage', 'color': ZWIFT_ORANGE, 'keys': [MacroPad.Keycode.T] })
actions.append({ 'name': 'end', 'displayname': 'End', 'color': NEGATIVE, 'keys': [MacroPad.Keycode.ESCAPE, MacroPad.Keycode.ENTER] })

# GUI
# TODO: Do a combined cycle of these? Like BOTH, HUD, GRAPH, NEITHER. Would save a spot
actions.append({ 'name': 'graph', 'displayname': 'Graph', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.G] })
actions.append({ 'name': 'hud', 'displayname': 'HUD', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.H] })

actions.append({ 'name': 'screenshot', 'displayname': 'ScShot', 'color': WHITE, 'keys': [MacroPad.Keycode.F10] })
actions.append({ 'name': 'powerup', 'displayname': 'PwrUp', 'color': POWERUP, 'keys': [MacroPad.Keycode.SPACEBAR] })
actions.append({ 'name': 'uturn', 'displayname': 'UTurn', 'color': ZWIFT_BLUE, 'keys': [MacroPad.Keycode.DOWN_ARROW] })
actions.append({ 'name': 'promo', 'displayname': 'Promo', 'color': WHITE, 'keys': [MacroPad.Keycode.P ] })

# Workouts
actions.append({ 'name': 'training', 'displayname': 'Train', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.E] })
actions.append({ 'name': 'skip', 'displayname': 'Skip', 'color': WARN, 'keys':[MacroPad.Keycode.TAB] })
actions.append({ 'name': 'bias_up', 'displayname': 'Bias+', 'color': POSITIVE, 'keys':[MacroPad.Keycode.PAGE_UP] })
actions.append({ 'name': 'bias_down', 'displayname': 'Bias-', 'color': NEGATIVE, 'keys':[MacroPad.Keycode.PAGE_DOWN] })
actions.append({ 'name': 'incline_up', 'displayname': 'Incl+', 'color': POSITIVE, 'keys':[MacroPad.Keycode.EQUALS] })
actions.append({ 'name': 'incline_down', 'displayname': 'Incl-', 'color': NEGATIVE, 'keys':[MacroPad.Keycode.MINUS] })
actions.append({ 'name': 'erg', 'displayname': 'Erg', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.UP_ARROW, MacroPad.Keycode.ENTER] })

# Camera
actions.append({ 'name': 'third', 'displayname': 'Third', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.ONE] })
actions.append({ 'name': 'third_short', 'displayname': 'ThShrt', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.TWO] })
actions.append({ 'name': 'first', 'displayname': 'First', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.THREE] })
actions.append({ 'name': 'angled', 'displayname': 'Angled', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.FOUR] })
actions.append({ 'name': 'chase', 'displayname': 'Chase', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.FIVE] })
actions.append({ 'name': 'rear', 'displayname': 'Rear', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.SIX] })
actions.append({ 'name': 'sideline', 'displayname': 'Sideline', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.SEVEN] })
actions.append({ 'name': 'helicopter', 'displayname': 'Heli', 'color': ZWIFT_BLUE, 'keys':[MacroPad.Keycode.EIGHT] })

# Emotes
actions.append({ 'name': 'elbow', 'displayname': 'Elbow', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F1] })
actions.append({ 'name': 'wave', 'displayname': 'Wave', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F2] })
actions.append({ 'name': 'ride_on', 'displayname': 'RdOn!', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F3] })
actions.append({ 'name': 'hammer_time', 'displayname': 'Hammer', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F4] })
actions.append({ 'name': 'nice', 'displayname': 'Nice', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F5] })
actions.append({ 'name': 'bring_it', 'displayname': 'BrngIt', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F6] })
actions.append({ 'name': 'toast', 'displayname': 'Toast', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F7] })
actions.append({ 'name': 'bell', 'displayname': 'Bell', 'color': ZWIFT_ORANGE, 'keys':[MacroPad.Keycode.F8] })

# Blank
actions.append({ 'name': 'blank', 'displayname': 'Blank', 'color': DISABLED, 'keys': [] })


def get_action_by_name(name):
  for action in actions:
    if action['name'] == name:
      return action
