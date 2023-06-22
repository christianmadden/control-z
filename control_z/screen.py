
from control_z import mode

def get_lines_for_mode(mode):
  lines = []
  labels = []
  for action in mode['actions']:
    labels.append(pad_action_label(action['displayname']))
  title = pad_title(f"{mode['displayname']} ")
  lines.append(f"{title} {mode['index'] + 1} of 6")
  lines.append(f"{labels[0]}{labels[1]}{labels[2]}")
  lines.append(f"{labels[3]}{labels[4]}{labels[5]}")
  lines.append(f"{labels[6]}{labels[7]}{labels[8]}")
  lines.append(f"{labels[9]}{labels[10]}{labels[11]}")
  return lines

def pad_action_label(label):
  return f"{label: <7}"

def pad_title(title):
  return f"{title:-<14}"