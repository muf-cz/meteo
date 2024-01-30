import requests
import datetime
import os
import imageio.v3 as imageio
from PIL import Image


def create_images_folder():
    folder_name = "images"

    # Zjistit aktuální pracovní adresář
    current_directory = os.getcwd()

    # Vytvořit cestu k adresáři "images"
    images_folder_path = os.path.join(current_directory, folder_name)

    # Zkontrolovat, zda složka již existuje
    if not os.path.exists(images_folder_path):
        # Pokud neexistuje, vytvořit ji
        os.makedirs(images_folder_path)
        print(f"Složka '{folder_name}' byla úspěšně vytvořena.")
    else:
        print(f"Složka '{folder_name}' již existuje.")
    return folder_name

create_images_folder()

for i in range(1,8):#tady se nastavuje pocet stažených snímku snimky jsou po 10min
    
    #image_name_dir = 'images/' + str(i) +'.png'
    #f = open(image_name_dir,'wb')

    x = datetime.datetime.now()
    hodina= (x.strftime("%H"))
    hodina = int(hodina)

    hodina = hodina -i -1
    hodina = str(hodina)
    if len(hodina) == 1:
        hodina="0"+hodina
    
    for a in range(0,60,10):
        image_name_dir = 'images/' + str(i) +str(a)+'.png'
        f = open(image_name_dir,'wb')
        minuta=a
        minuta= str(minuta)
        if minuta=="0":
            minuta="00"
        #else:
        #    minuta=int(minuta)+10
        
        print (hodina)
        soubor= (x.strftime("%Y%m%d." + str(hodina) + ""+str(minuta)))
        print (soubor)
        request_url = 'https://www.chmi.cz/files/portal/docs/meteo/rad/inca-cz/data/czrad-z_max3d/'+ 'pacz2gmaps3.z_max3d.' + soubor + '.0.png'
        print (request_url)

        r = requests.get(request_url)
        if r.status_code == 200:
            f.write(requests.get(request_url).content)
            f.close()

            print(image_name_dir + ' is successfully downloaded.')

        else: 
            print('Error. Image cannot be retrieved.')
            os.remove("images/" + str(i) +str(a)+".png")
            break

    # Front Image
        filename = 'images/' + str(i) +str(a)+'.png'
  
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
        background.save("images/new"+str(i-10)+str(a)+".png", format="png")
        os.remove("images/" + str(i) +str(a)+".png")

png_dir = create_images_folder()
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.imwrite('meteo.gif', images,fps=5)

print ("gif vytvořen")


