from PIL import Image, ImageDraw, ImageFilter
import random, math, string, os, sys
from datetime import datetime as dt
#from drawtools import circle, box, triangle, gradient, gradient2

# drawings Lissajous in Python
# (c)2018 MoNsTeR/GDC, Noniewicz.com, Jakub Noniewicz
# https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
# cre: 20180503
# upd; 2018????

# TODO:
# - ?

def liss(draw, params):
    c = math.pi/180
    FF1 = params['FF1']
    FF2 = params['FF2']
    Time = 0
    if FF2 > 0:
        Freq = FF1/FF2
    else:
        Freq = 0
    Fi = params['FFi'] # *math.pi
    sx = params['w']/2
    sy = params['h']/2
    if sx > sy:
        ampli = sy*params['Scale']
    else:
        ampli = sx*params['Scale']

    for i in range(params['Steps']):
        x = int(sx+ampli*math.sin(c*Time))
        y = int(sy+ampli*math.sin(c*(Time*Freq+Fi)))
        if i == 0:
            points = ((x, y), (x, y))
        else:
            points = (points[1], (x, y))
        draw.line(points, fill=params['LineColor'], width=params['LineWidth'])
        Time = Time + params['dT']

# ---

def call_painter(params, png):
    start_time = dt.now()
    print('drawing...', png)
    im = Image.new('RGB', (params['w'], params['h']), params['Background'])
    draw = ImageDraw.Draw(im)

    # note: loop - test only
    for z in range(10):
        liss(draw, params)
        params['FFi'] = params['FFi'] + 2

    im.save(png, dpi=(300,300))
    time_elapsed = dt.now() - start_time
    print('done. elapsed time: {}'.format(time_elapsed))

# ---

w = 4960
h = 3507

params1 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (255,255,255),
    'LineWidth': 10,
    'FF1': 19.0,
    'FF2': 31.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}
call_painter(params1, 'liss-0001.png')

params2 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (50,255,50),
    'LineWidth': 10,
    'FF1': 3.0,
    'FF2': 4.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}
call_painter(params2, 'liss-0002.png')

params3 = {
    'w': w, 'h': h,
    'Background': (0, 0, 0),
    'LineColor': (50,255,50),
    'LineWidth': 10,
    'FF1': 2.0,
    'FF2': 3.0,
    'FFi': 0,
    'dT': 1,
    'Steps': 2000,
    'Scale': 0.9,
}
call_painter(params3, 'liss-0003.png')
