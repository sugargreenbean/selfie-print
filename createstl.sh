#!/bin/bash
magick convert static/outlinedselfie.jpg static/pngoutline.png
convert static/pngoutline.png static/pnmoutline.pnm
potrace -s -o static/vectorselfie.svg static/pnmoutline.pnm
