# import library opoencv dan di berikan variable dengan nama cv
import cv2 as cv
import numpy as np




image = cv.imread('anyaForger.jpeg')



dimension = image.shape
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]

w, h = (145, 50)
temp = cv.resize(image, (w, h), interpolation=cv.INTER_LINEAR)

output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)

# Menambahkan teks ke dalam gambar
# text = f'Dimensi: {dimension}, Height: {height}px, Width: {width}px, Channels: {channels}'

textLines = [
    f'Dimensi: {dimension}',
    f'Height: {height}px',
    f'Width: {width}px',
    f'Channels: {channels}'
]

font = cv.FONT_HERSHEY_DUPLEX
font_scale = 0.4
color = (255, 255, 255)  # Warna putih
thickness = 0
position = (20, 155)  # Posisi teks (x, y)
# cv.putText(output, text, position, font, font_scale, color, thickness, cv.LINE_AA)

for i, line in enumerate(textLines):
        cv.putText(output, line, (position[0], position[1] + i * 20), font, font_scale, color, thickness, cv.LINE_AA)



print('dimension is', dimension)
print('height is', height, "px")
print('width is', width, "px")
print('channel is', channels)

# windows_name = 'image'

# cv.imshow(windows_name, image)
cv.imshow('input', image)
cv.imshow('output', output)



cv.waitKey(0)
cv.destroyAllWindows()