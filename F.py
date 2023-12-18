# Legge til en fotoramme eller kant rundt selve bildet
# from Tkinter import *
# from PIL import Image
# import pilgram

# bilde = Image.open('sample.jpg')

# backround = #FDF0A9
# left = -10
# top = -10
# right = 1110
# bottom =1110

# bilde1 = bilde.widen((left, top, right, bottom))

# bilde1.save('sample-polaroidbilde.jpg')



# canvas = Canvas(width = 1100, height = 1110, bg = 'white')
# canvas.pack(expand = YES, fill = BOTH)

# image = ImageTk.PhotoImage(file = "sample-resized.jpg")
# canvas.create_image(10, 10, image = image, anchor = NW)

# polaroidbilde = image

# polaroidbilde.save('sample-polaroidbilde.jpg')

# from tkinter import Tk
# from PIL import Image

# bilde = Image.open('sample-resize.jpg')

# vindu = Tk()

# vindu.configure(bg="#FDF0A9")

# bakgrunn = vindu

# bakgrunn.save('sample-polaroidbilde.jpg')

# vindu.mainloop()


# from tkinter import Tk, Label   
# from PIL import ImageTk, Image

# vindu = Tk()

# bilde = Image.open('sample-resize.jpg')

# bakgrunnsbilde = ImageTk.PhotoImage(bilde)


# Lable = Label(vindu, Image = bakgrunnsbilde)
# Lable.place (x = -10, y = -10, relheight = 1110, relwidth= 1110)

# vindu.mainloop()



# from PIL import Image 
# import pilgram 

# bilde = Image.open('sample.jpg')

# width, height = bilde.size

# left = 0
# top = 0
# right = 1080
# bottom = 1080

# bilde1 = bilde.crop((left, top, right, bottom))
# newsize = (1080, 1080)
# bilde1 = bilde1.resize(newsize)

# bilde1.save('sample-croped.jpg')


# def resize_Image(input_path, output_path, new_size=(760, 760)):
#     with Image.open(input_path) as img:
#         resized_img = img.resize(new_size)

#         resized_img.save(output_path)


# resize_Image('sample-croped.jpg', 'sample-polaroid.jpg')

# ramme = Image.open('polaroid-frame-PNG-5.png')

# bilde = Image.open('sample-polarodi.jpg')

# polaroidbilde = ramme.paste(bilde, (64,64))

# polaroidbilde.save('sample-polaroidbilde.jpg')

from PIL import Image, Image, ImageOps

input_path = 'sample.jpg'
polaroid_frame_path = 'polaroid-frame-PNG-5.png'
output_path = 'bilde-polaroid.jpg'


# Åpner bildet
original_bilde = Image.open(input_path)

# Beskjær til 1:1 høyde-breddeforhold
beskjært_bilde = ImageOps.fit(original_bilde, (min(original_bilde.size), min(original_bilde.size)))

# Skaler bildet til passende størrelse for den polaroide fotorammen (760x760)
skalert_bilde = beskjært_bilde.resize((760, 760))

# Åpne polaroid-ramme PNG-filen
polaroid_ramme = Image.open(polaroid_frame_path)

# Opprett en ny bildebeholder med hvit bakgrunn. Et canvas
ramme_bilde = Image.new("RGB", (880, 1040), 'white')

# Legg til polaroid-ramme på toppen
ramme_bilde.paste(polaroid_ramme)

# Legg til det skalerte bildet i bildebeholderen med en offset på 64 piksler i x- og y-retning
ramme_bilde.paste(skalert_bilde, (64, 64))

# Lagre det endelige bildet
ramme_bilde.save(output_path)