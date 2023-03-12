def calc_pyramid_volume(base_length, base_width, pyramid_height):
    area = length * width
    return area * height * 1/3

length = float(input('Length: '))
width = float(input('Width: '))
height = float(input('Height: '))
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))