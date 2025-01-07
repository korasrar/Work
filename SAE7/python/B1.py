from PIL import Image

"""i=Image.open("/home/koras/Work/SAE7/Image3.bmp")
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel((x,y))
        print(c),
    print("")"""

"""i=Image.open("/home/koras/Work/SAE7/Image3.bmp")
sorite=i.copy()
sortie.save("/home/koras/Work/SAE7/Imageout.bmp")"""

"""i=Image.open("/home/koras/Work/SAE7/Image0.bmp")
sortie=i.copy()
sortie.putpixel((1,2),(0,0,255))
sortie.save("/home/koras/Work/SAE7/Imageout.bmp")"""

"""i=Image.open("/home/koras/Work/SAE7/Image0.bmp")
sortie=i.copy()
sortie.putpixel((1,2),(0,0,255))
sortie.save("/home/koras/Work/SAE7/Imageout.bmp")"""

# Reponse : 
def transpose(filebmp):
    i=Image.open(filebmp)
    sortie=Image.new(i.mode,i.size)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            sortie.putpixel((x,y),i.getpixel((y,x)))
    sortie.save("SAE7/Imageout0.bmp")
