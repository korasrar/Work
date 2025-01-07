from PIL import Image

# Reponse : 
def nuancegris(filebmp):
    i=Image.open(filebmp)
    sortie=Image.new(i.mode,i.size)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            pixel = i.getpixel((x,y))
            newpixel = (pixel[0]+pixel[1]+pixel[2])//3
            sortie.putpixel((x,y),(newpixel,newpixel,newpixel))
    sortie.save("SAE7/Imageout2.bmp")
print(miroir("SAE7/IUT-Orleans.bmp"))