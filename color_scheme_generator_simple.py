import math
import random
import colorsys

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
        "red":None,
        "green":None,
        "blue":None
     },
    "Color 2": {
        "hue":None,
        "red":None,
        "green":None,
        "blue":None
    },
    "Color 3": {
        "hue":None,
        "red":None,
        "green":None,
        "blue":None
    },
    "Color 4": {
        "hue":None,
        "red":None,
        "green":None,
        "blue":None
    }
}

# Check to see if 0.0 < hue < 1.0, correct hue if needed
def correct_hue(hue): 
    if hue < 0:   
        hue = abs(hue) 
    if hue > 1.0:
        hue -= 1.0 
    return hue  

# Generate the same hue
def monochromatic(hue): 
    return hue
# This function could be improved by generating additional shades

# Generate a hue exactly 180 degrees from the original hue
def complementary(hue): 
    hue1 = correct_hue(hue + 0.5)
    return hue1

# Generate two hues +/- 150 degrees from original hue
def split_complementary(hue): 
    hue1 = correct_hue(hue + 0.58333)
    hue2 = correct_hue(hue - 0.58333)
    return hue1, hue2

# Generate two hues +/- 30 degrees from original hue
def analogous(hue): 
    hue1 = correct_hue(hue + 0.08333)
    hue2 = correct_hue(hue - 0.08333) 
    return hue1, hue2 

# Generate two hues +/- 120 degrees from original hue
def triad(hue): 
    hue1 = correct_hue(hue + 0.8333)      
    hue2 = correct_hue(hue - 0.8333)
    return hue1, hue2

# Generate three hues 60, 180, and 240 degrees from the original hue
def analogous_tetrad(hue): 
    hue1 = correct_hue(hue + 0.1666)
    hue2 = correct_hue(hue + 0.5)
    hue3 = correct_hue(hue2 + 0.1666)
    return hue1, hue2, hue3

# Generate three hues 90, 180, and 270 degrees from the original hue
def complementary_tetrad(hue):
    hue1 = correct_hue(hue + 0.5)
    hue2 = correct_hue(hue1 + 0.25)
    hue3 = correct_hue(hue1 - 0.25)
    return hue1, hue2, hue3

# Conversion to scale value for RGB
def convert_comp(color):
    color *= 255
    color = math.floor(color)
    return color

# Convert HSV to RGB
def convert_rgb(hue): 
    red, green, blue = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    red = convert_comp(red)
    green = convert_comp(green)
    blue = convert_comp(blue)
    return red, green, blue

# Convert RGB to hex value (if desired)
#def convert_hex(red, green, blue):
#   hex = '#%02x%02x%02x' % (red, green, blue)
#   return hex
# Add hex to the dictionary below with "hex":None after "blue":None

# Randomly choose a scheme type, report the chosen type
scheme = random.choice(scheme_types)
print('Scheme Type:',scheme)

# Randomly choose a hue for 'Color 1'
color_set['Color 1']['hue'] = random.random()

if scheme == 'Monochromatic':
    color_set['Color 2']['hue'] = monochromatic(color_set['Color 1']['hue'])
    
elif scheme == 'Complementary':
    color_set['Color 2']['hue'] = complementary(color_set['Color 1']['hue'])

elif scheme == 'Split-Complementary':
    color_set['Color 2']['hue'], \
    color_set['Color 3']['hue'] \
    = split_complementary(color_set['Color 1']['hue'])

elif scheme == 'Analogous':
    color_set['Color 2']['hue'], \
    color_set['Color 3']['hue'] \
    = analogous(color_set['Color 1']['hue']) 
    
elif scheme == 'Triad':
    color_set['Color 2']['hue'], \
    color_set['Color 3']['hue'] \
    = triad(color_set['Color 1']['hue'])

elif scheme == 'Analogous-Tetrad':
    color_set['Color 2']['hue'], \
    color_set['Color 3']['hue'], \
    color_set['Color 4']['hue'] \
    = analogous_tetrad(color_set['Color 1']['hue'])

elif scheme == 'Complementary-Tetrad':
    color_set['Color 2']['hue'], \
    color_set['Color 3']['hue'], \
    color_set['Color 4']['hue'] \
    = complementary_tetrad(color_set['Color 1']['hue'])

# Loop through all used colors to convert HSV to RGB
for color,colortype in color_set.items():
    if color_set[color]['hue'] != None:
        color_set[color]['red'], \
        color_set[color]['green'], \
        color_set[color]['blue'] \
        = convert_rgb(color_set[color]['hue'])
# Use a similar loop to populate hex values using convert_hex if desired

# Loop through all used colors and report RGB values
for color,colortype in color_set.items():
    if color_set[color]['hue'] != None:
        print('\n' + str(color) + ':')
        for valuetype,value in colortype.items():
            if valuetype != 'hue':
                print(valuetype, value)