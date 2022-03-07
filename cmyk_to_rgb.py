#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ee = '\033[1m'
green = '\033[32m'
yellow = '\033[33m'
cyan = '\033[36m'

line = cyan+'-' * 0x2D
print(ee+line)

C,M,Y,K = [float(X) / 0x64 for X in input(yellow+'CMYK: '+green).split()]
R,G,B = [round(0xFF * (1-X) * (1-K)) for X in [C,M,Y]]

print(f'{yellow}RGB: {green}{R}, {G}, {B}')
print(line)
