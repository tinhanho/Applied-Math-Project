from PIL import Image

img = Image.open("1.jpg")
img = img.resize((1056, 1920))

img.save('PIL.jpg')