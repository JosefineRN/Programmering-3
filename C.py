#Funksjonalitet for å kunne rotere bildet enten 90 grader med klokka, 90 grader mot klokka eller 180 grader.
from PIL import Image
import pilgram

bilde = Image.open('sample.jpg')
rotert_180 = bilde.rotate(180)
rotert_h = bilde.rotate(-90)
rotert_v = bilde.rotate(90)

bruker = input("Skriv inn '90 grader til høyre', '90 grader til venstre' eller '180 grader' for å rotere bildet ditt:")

if bruker == "90 grader til høyre":

    rotert_h = bilde.rotate(-90).save ('sample-rotert_h.jpg')

elif bruker == "90 grader til venstre":

    rotert_v = bilde.rotate(90).save ('sample-rotert_v.jpg')

elif bruker == "180 grader":
    rotert_180 = bilde.rotate(180).save ('sample-rotert_180.jpg')

else:
    print ("verdien de skrev inn er ikke gyldig")





