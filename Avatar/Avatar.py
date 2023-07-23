from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
shift = 25
coordinates = (shift * 2, 0, red.width, red.height)
red1 = image.crop(coordinates) 
coordinates = (shift, 0, red.width-shift, red.height)
red_left = image.crop(coordinates)
red_blend = Image.blend(red1, red_left, 0.3)
coordinates = (0, 0, blue.width-50, blue.height)
blue1 = image.crop(coordinates) 
coordinates = (shift, 0, blue.width-shift, blue.height)
blue_right = image.crop(coordinates)
blue_blend = Image.blend(blue_right, blue1, 0.3)
coordinates = (shift, 0, green.width-shift, green.height)
green1 = image.crop(coordinates) 
new_image = Image.merge("RGB", (red_blend.convert('L'), green1.convert('L'), blue_blend.convert('L')))
new_image.thumbnail((80, 80)) 
new_image.save('monro_avatar.jpg')

