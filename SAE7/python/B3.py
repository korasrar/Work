from PIL import Image

# Reponse : 
def miroir(filebmp):
    i=Image.open(filebmp)
    sortie=Image.new(i.mode,i.size)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            sortie.putpixel((x,y),i.getpixel((-x,y)))
    sortie.save("SAE7/Imageout1.bmp")
print(miroir("SAE7/hall-mod_0.bmp"))