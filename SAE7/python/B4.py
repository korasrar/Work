from PIL import Image

# Reponse : 
def noiretblanc(filebmp):
    i=Image.open(filebmp)
    sortie=Image.new(i.mode,i.size)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            pixel = i.getpixel((x,y))
            if (pixel[0]*pixel[0]+pixel[1]*pixel[1]+pixel[2]*pixel[2])>255*255*3//2:
                sortie.putpixel((x,y),(255,255,255))
            else :
                sortie.putpixel((x,y),(0,0,0))
    sortie.save("SAE7/Imageout3.bmp")
print(noiretblanc("SAE7/IUT-Orleans.bmp"))