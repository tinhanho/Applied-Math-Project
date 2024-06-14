from PIL import Image

img = Image.open("2.jpg")
img = img.resize((2400, 1350))

img.save('PIL.jpg')