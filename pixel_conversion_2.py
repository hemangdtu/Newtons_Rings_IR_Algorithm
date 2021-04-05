#!/usr/bin/env python3
import sys
import numpy as np

with open("output.txt", 'r') as my_file:
    pixels = my_file.read().split('\n')[:-1]

val = input()

if val == 1:
    firstDist = float("62")
else:
    firstDist = float("53")

file1 = open(r"converted.txt","w")
# [print(i/88.33311) for i in np.array(pixels).astype(np.float32) * firstDist / (float(pixels[1]) - float(pixels[0]))]
for i in np.array(pixels).astype(np.float32) * firstDist / (float(pixels[1]) - float(pixels[0])):
    file1.write(str(i/88.33311)+"\n")
file1.close()
