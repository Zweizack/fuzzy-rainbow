#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ee = '\033[1m'
green = '\033[32m'
yellow = '\033[33m'
cyan = '\033[36m'

line = cyan+'-' * 0x2D
print(ee+line)

Hex = input(ee+yellow+'Hex: '+ee+green)
print(ee+line)

R,G,B = [int(X,16) for X in [Hex[2:4],Hex[4:6],Hex[6:8]]]
print(f'{yellow}RGB:  {green}({R},{G},{B})')

R,G,B = [X / 0xFF for X in [R,G,B]]

K = 1-max(R,G,B)
C,M,Y = [round(float((1-X-K)/(1-K) * 0x64),1) for X in [R,G,B]]
K = round(K * 0x64,1)

print(f'{yellow}CMYK: {green}{C}%, {M}%, {Y}%, {K}%')
print(line)
