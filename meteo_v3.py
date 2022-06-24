import requests
import datetime
import os
import imageio.v2 as imageio
from PIL import Image

for i in range(1,10):
    
    image_name_dir = 'images/' + str(i) + '.png'
    f = open(image_name_dir,'wb')

    x = datetime.datetime.now()
    hodina= (x.strftime("%H"))
    hodina = int(hodina)

    hodina = hodina -i -1
    hodina = str(hodina)
    if len(hodina) == 1:
        hodina="0"+hodina
    
    
    print (hodina)
    soubor= (x.strftime("%Y%m%d." + str(hodina) + "00"))
    request_url = 'https://www.chmi.cz/files/portal/docs/meteo/rad/inca-cz/data/czrad-z_max3d/'+ 'pacz2gmaps3.z_max3d.' + soubor + '.0.png'
      

    r = requests.get(request_url)
    if r.status_code == 200: 
        f.write(requests.get(request_url).content)
        f.close()

        print(image_name_dir + ' is successfully downloaded.')

    else: 
        print('Error. Image cannot be retrieved.')

    # Front Image
    filename = 'images/'+ str(i) +'.png'
  
    # Back Image
    filename1 = 'mapa4.png'
  
    # Open Front Image
    frontImage = Image.open(filename)
  
    # Open Background Image
    background = Image.open(filename1)
  
    # Convert image to RGBA
    frontImage = frontImage.convert("RGBA")
  
    # Convert image to RGBA
    background = background.convert("RGBA")
  
    # Calculate width to be at the center
    width = (background.width - frontImage.width) // 2
  
    # Calculate height to be at the center
    height = (background.height - frontImage.height) // 2
  
    # Paste the frontImage at (width, height)
    background.paste(frontImage, (width, height), frontImage)
  
    # Save this image
    background.save("images/new"+str(i-10)+".png", format="png")
    os.remove("images/"+str(i)+".png")

png_dir = '/home/noname/Desktop/meteoradar/images'
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('meteo.gif', images,fps=1)
        