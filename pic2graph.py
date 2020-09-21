#!/usr/bin/env python3

from PIL import Image
from sys import argv, exit

if len(argv) < 3:
    print('usage: {} [input] [output]'.format(argv[0]))
    exit(1)

input = Image.open(argv[1]).convert('RGB')
output = open(argv[2], 'w')

headerf = open('header.graphml', 'r')
header = headerf.read(100000)
headerf.close()

footerf = open('footer.graphml', 'r')
footer = footerf.read(100000)
footerf.close()

pixelf = open('pixel.graphml', 'r')
pixel = pixelf.read(100000)
pixelf.close()

output.write(header)
for x in range(input.width):
    for y in range(input.height):
        c = ''
        for channel in input.getpixel((x, y)):
            c += hex(channel)[2:]
        output.write(pixel
                .replace('$ID$', str(x * input.height + y))
                .replace('$X$', str(x * 20))
                .replace('$Y$', str(y * 20))
                .replace('$COLOR$', c))
output.write(footer)
