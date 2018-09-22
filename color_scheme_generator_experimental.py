import math
import random
import colorsys
import webbrowser
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtCore import Qt

#there are 7 possible scheme types
scheme_types = ['Monochromatic', 
'Complementary', 
'Split-Complementary', 
'Analogous', 
'Triad', 
'Analogous-Tetrad', 
'Complementary-Tetrad']

# color_set is a dictionary for generated colors and their values
color_set = {
    "Color 1": {
        "hue":None,
        "saturation":None,
        "value":None,
        "red":None,
        "green":None,
        "blue":None,
        "hex":None
     },
    "Color 2": {
        "hue":None,
        "saturation":None,
        "value":None,
        "red":None,
        "green":None,
        "blue":None,
        "hex":None
    },
    "Color 3": {
        "hue":None,
        "saturation":None,
        "value":None,
        "red":None,
        "green":None,
        "blue":None,
        "hex":None
    },
    "Color 4": {
        "hue":None,
        "saturation":None,
        "value":None,
        "red":None,
        "green":None,
        "blue":None,
        "hex":None
    }
}

# Easy way to sort colors by desired order
color_order = {'Color 1':1, 'Color 2':2, 'Color 3':3, 'Color 4':4}

# Check to see if 0.0 < hue < 1.0, correct hue if needed
def correct_hue(hue): 
    if hue < 0:   
        hue = abs(hue) 
    if hue > 1.0:
        hue -= 1.0 
    return hue  

# Generate the same hue with different saturation and value
def monochromatic(hue): 
    hue1 = hue
    saturation1 = randnum_scaled()
    value1 = randnum_scaled()
    return hue1, saturation1, value1

# Generate a hue exactly 180 degrees from the original hue
def complementary(hue): 
    hue1 = correct_hue(hue + 0.5)
    saturation1 = randnum_scaled()
    value1 = randnum_scaled()
    return hue1, saturation1, value1

# Generate two hues +/- 150 degrees from original hue
def split_complementary(hue): 
    hue1 = correct_hue(hue + 0.4167)
    hue2 = correct_hue(hue - 0.4167)
    saturation1 = randnum_scaled()
    saturation2 = randnum_scaled()
    value1 = randnum_scaled()
    value2 = randnum_scaled()
    return hue1, saturation1, value1, hue2, saturation2, value2

# Generate two hues +/- 30 degrees from original hue
def analogous(hue): 
    hue1 = correct_hue(hue + 0.08333)
    hue2 = correct_hue(hue - 0.08333)
    saturation1 = randnum_scaled()
    saturation2 = randnum_scaled()
    value1 = randnum_scaled()
    value2 = randnum_scaled()
    return hue1, saturation1, value1, hue2, saturation2, value2

# Generate two hues +/- 120 degrees from original hue
def triad(hue): 
    hue1 = correct_hue(hue + 0.3333)      
    hue2 = correct_hue(hue1 + 0.3333)
    saturation1 = randnum_scaled()
    saturation2 = randnum_scaled()
    value1 = randnum_scaled()
    value2 = randnum_scaled()
    return hue1, saturation1, value1, hue2, saturation2, value2

# Generate three hues 60, 180, and 240 degrees from the original hue
def analogous_tetrad(hue): 
    hue1 = correct_hue(hue + 0.1666)
    hue2 = correct_hue(hue + 0.5)
    hue3 = correct_hue(hue2 + 0.1666)
    saturation1 = randnum_scaled()
    saturation2 = randnum_scaled()
    saturation3 = randnum_scaled()
    value1 = randnum_scaled()
    value2 = randnum_scaled()
    value3 = randnum_scaled() 
    return hue1, saturation1, value1, hue2, saturation2, value2, hue3, saturation3, value3

# Generate three hues 90, 180, and 270 degrees from the original hue
def complementary_tetrad(hue):
    hue1 = correct_hue(hue + 0.5)
    hue2 = correct_hue(hue1 + 0.25)
    hue3 = correct_hue(hue1 - 0.25)
    saturation1 = randnum_scaled()
    saturation2 = randnum_scaled()
    saturation3 = randnum_scaled()
    value1 = randnum_scaled()
    value2 = randnum_scaled() 
    value3 = randnum_scaled()
    return hue1, saturation1, value1, hue2, saturation2, value2, hue3, saturation3, value3

# Conversion to scale value for RGB
def convert_comp(color):
    color *= 255
    color = math.floor(color)
    return color

# Convert HSV to RGB
def convert_rgb(hue, saturation, value): 
    red, green, blue = colorsys.hsv_to_rgb(hue, saturation, value)
    red = convert_comp(red)
    green = convert_comp(green)
    blue = convert_comp(blue)
    return red, green, blue

def randnum_scaled():
    randnum = 0.75*random.random() + 0.25
    return randnum

# Convert RGB to hex value (if desired)
def convert_hex(red, green, blue):
  hex = '%02x%02x%02x' % (red, green, blue)
  return hex

print('-'.rjust(34,'-'))

# Randomly choose a scheme type, report the chosen type
scheme = random.choice(scheme_types)
print('Scheme Type:' ,scheme, '\n')

# Randomly set HSV for 'Color 1'
color_set['Color 1']['hue'] = random.random()
color_set['Color 1']['saturation'] = randnum_scaled()
color_set['Color 1']['value'] = randnum_scaled()
# Saturation & value scaled above 0.25 to prevent grey, black, or white

if scheme == 'Monochromatic':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'] \
    = monochromatic(color_set['Color 1']['hue'])

elif scheme == 'Complementary':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'] \
    = complementary(color_set['Color 1']['hue'])

elif scheme == 'Split-Complementary':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'], \
    color_set['Color 3']['hue'], \
    color_set['Color 3']['saturation'], \
    color_set['Color 3']['value'] \
    = split_complementary(color_set['Color 1']['hue'])

elif scheme == 'Analogous':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'], \
    color_set['Color 3']['hue'], \
    color_set['Color 3']['saturation'], \
    color_set['Color 3']['value'] \
    = analogous(color_set['Color 1']['hue']) 
    
elif scheme == 'Triad':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'], \
    color_set['Color 3']['hue'], \
    color_set['Color 3']['saturation'], \
    color_set['Color 3']['value'] \
    = triad(color_set['Color 1']['hue'])

elif scheme == 'Analogous-Tetrad':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'], \
    color_set['Color 3']['hue'], \
    color_set['Color 3']['saturation'], \
    color_set['Color 3']['value'], \
    color_set['Color 4']['hue'], \
    color_set['Color 4']['saturation'], \
    color_set['Color 4']['value'] \
    = analogous_tetrad(color_set['Color 1']['hue'])

elif scheme == 'Complementary-Tetrad':
    color_set['Color 2']['hue'], \
    color_set['Color 2']['saturation'], \
    color_set['Color 2']['value'], \
    color_set['Color 3']['hue'], \
    color_set['Color 3']['saturation'], \
    color_set['Color 3']['value'], \
    color_set['Color 4']['hue'], \
    color_set['Color 4']['saturation'], \
    color_set['Color 4']['value'] \
    = complementary_tetrad(color_set['Color 1']['hue'])     

print('RED'.rjust(16), 'GREEN'.rjust(8), 'BLUE'.rjust(8))
for color in sorted(color_order, key=color_order.__getitem__):
    if color_set[color]['hue'] != None:
        
        color_set[color]['red'], \
        color_set[color]['green'], \
        color_set[color]['blue'] \
        = convert_rgb(color_set[color]['hue'], 
        color_set[color]['saturation'], 
        color_set[color]['value'])
        
        color_set[color]['hex'] = convert_hex(color_set[color]['red'], 
            color_set[color]['green'], 
            color_set[color]['blue'])
        
        webbrowser.open_new("https://www.google.com/search?q=%23"+str(color_set[color]['hex']))
    
        print('{0:7} {1:8} {2:8} {3:8}'.format(
            color, 
            color_set[color]['red'], 
            color_set[color]['green'], 
            color_set[color]['blue']))
print('-'.rjust(34,'-'))       