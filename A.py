#Kunne legge på et Instagram-ready filter på bildet (velg et passende filter fra pilgram)
from PIL import Image
import pilgram

bilde = Image.open('sample.jpg')
pilgram.kelvin(bilde).save('sample-kelvin.jpg')

