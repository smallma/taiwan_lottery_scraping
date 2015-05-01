from lib.pytesser.pytesser import *


def test(filename):
	print filename
	# image = Image.open(filename)  # Open image object using PIL
	# print image_to_string(image)     # Run tesseract.exe on image
	print image_file_to_string('test.tif')

def test2():
	import PIL
	from PIL import ImageFont
	from PIL import Image
	from PIL import ImageDraw
	img=Image.new("RGBA", (200,200),(120,20,20))
	draw = ImageDraw.Draw(img)
	draw.text((0, 0),"This is a test",(255,255,0))
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)
	img.save("a_test.png")

	print image_to_string(img) 