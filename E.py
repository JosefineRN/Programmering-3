#Beskjære bildet etter Instagrams offisielle spesifikasjoner for bredde- og høydeformat, som sier at bilder skal ligge mellom 1.91:1 og 4:5. Kontroller at bredden er på minimum 1080px. Les mer her: https://help.instagram.com/1631821640426723from PIL import Image
import pilgram

bilde = image.open('sample.jpg')

# new_width = 1350
# new_height = 1080

# bilde = bilde.resize ((new_width, new_height), Image.ANTIALIAS)


# bilde.save('sample-croped.jpg')



# height = 1350
# width = 1080

# bilde1 = bilde.crop(height, width)

# newsize = (height, width)

# bilde.resize(newsize)

# bilde.reszie.save ('sample-croped.jpg')


width, height = bilde.size

left = 0
top = 0
right = 1080
bottom = 1080

bilde1 = bilde.crop((left, top, right, bottom))
newsize = (1350, 1080)
bilde1 = bilde1.resize(newsize)

bilde1.save('sample-croped.jpg')



