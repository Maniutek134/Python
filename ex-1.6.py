from PIL import Image

fileJpg=input("enter file name")
nameJpg = fileJpg + '.jpg'
namePng = fileJpg+ '.png'

im = Image.open(nameJpg)
im.save(namePng)