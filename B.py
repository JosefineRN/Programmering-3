#Kunne legge på et black & white art filter (velg et passende filter fra pilgram)
from PIL import Image
import pilgram

bilde = Image.open('sample.jpg')
pilgram.willow(bilde).save('sample-willow.jpg')

