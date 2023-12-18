# Finn en måte å sammensy de ulike funksjonene i oppgavene a til g. 

from PIL import Image, Image, ImageOps
import pilgram 


A = print("A) Sette filter på bildet")
B = print("B) Rotere bildet")
C = print("C) Skalere bildet")
D = print("D) Beskjære bildet")
E = print("E) Gjøre det om til et polaroid bildet")

# Spør burkeren hva de vil gjøre med bildet

første_valg = input("Hva øsnker du å gjøre med bildet (skriv bokstaven til valget du vil ta)?") #A) Sette filter på bildet, B) Rotere bildet, C) Skalere bildet, D) Beskjære bildet, E) Gjøre det om til et polaroid bildet")


# Spør brukeren hviket filter de vil gi bildet og legger til filteret som brukeren valgte
if første_valg == A:
    print ("Hvilket filter vil du gi bildet? (skriv bokstaven til valget du vil ta), A) 1977, B) Aden, C) Willow, D) Kelvin, E) Ciarendon ")

if første_valg == A:
    bilde = Image.open('sample.jpg')
    pilgram._19771977(bilde).save('sample-1977.jpg')

elif første_valg == B:
    bilde = Image.open('sample.jpg')
    pilgram.aden(bilde).save('sample-aden.jpg')

elif første_valg== C:
    bilde = Image.open('sample.jpg')
    pilgram.willow(bilde).save('sample-willow.jpg')

elif første_valg == D:
    bilde = Image.open('sample.jpg')
    pilgram.kelvin(bilde).save('sample-kelvin.jpg')

elif første_valg == E:
    bilde = Image.open('sample.jpg')
    pilgram.Ciarendon(bilde).save('sample-ciarendon.jpg')

# Hvis en annen verdi blir tastet vil den printe "ugyldig, prøv igjen" og du må kjøre prøgramet igjen

else:
    print("Ugyldig, prøv igjen")



første_valg3 = input("Hvor mange grader vil du rotere bildet")








# input_path = 'sample.jpg'
# polaroid_frame_path = 'polaroid-frame-PNG-5.png'
# output_path = 'bilde-polaroid.jpg'


# # Åpner bildet
# original_bilde = Image.open(input_path)

# # Beskjær til 1:1 høyde-breddeforhold
# beskjært_bilde = ImageOps.fit(original_bilde, (min(original_bilde.size), min(original_bilde.size)))

# # Skaler bildet til passende størrelse for den polaroide fotorammen (760x760)
# skalert_bilde = beskjært_bilde.resize((760, 760))

# # Åpne polaroid-ramme PNG-filen
# polaroid_ramme = Image.open(polaroid_frame_path)

# # Opprett en ny bildebeholder med hvit bakgrunn. Et canvas
# ramme_bilde = Image.new("RGB", (880, 1040), 'white')

# # Legg til polaroid-ramme på toppen
# ramme_bilde.paste(polaroid_ramme)

# # Legg til det skalerte bildet i bildebeholderen med en offset på 64 piksler i x- og y-retning
# ramme_bilde.paste(skalert_bilde, (64, 64))

# # Lagre det endelige bildet
# ramme_bilde.save(output_path)