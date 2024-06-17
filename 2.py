from PIL import Image

img = Image.open("1.jpg")
img = img.resize((33, 60))

img.save('PIL.jpg')