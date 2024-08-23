"""Extracts colors from an image."""

import colorgram

colors = colorgram.extract('static/image.jpg', 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

color_list_rgb = [tuple(c/255 for c in color) for color in color_list]
