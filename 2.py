from PIL import Image

img = Image.open("david.jpg")
img = img.resize((144, 96))

img.save('david144.jpg')