from PIL import Image

def cacher(i,b):
    return i-(i%2)+b

def trouver(i):
    return i%2

def steganographiecacher(filetohide,filehost):
    hide=Image.open(filetohide)
    host=Image.open(filehost)
    sortie=Image.new(host.mode,host.size)
    for y in range(hide.size[1]):
        for x in range(hide.size[0]):
            pixelhide = hide.getpixel((x,y))
            pixelhost = host.getpixel((x,y))
            if pixelhide == (0,0,0):
                sortie.putpixel((x,y),(cacher(pixelhost[0],1),pixelhost[1],pixelhost[2]))
            else :
                sortie.putpixel((x,y),host.getpixel((x,y)))
    sortie.save("SAE7/Imageout_steg_1.bmp")
print(steganographiecacher("SAE7/Imageout3.bmp","SAE7/Imageout_steg_0.bmp"))

def steganographietrouver(filebmp):
    i=Image.open(filebmp)
    sortie=Image.new(i.mode,i.size)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            pixel = i.getpixel((x,y))
            if pixel == (cacher(pixel[0],1),pixel[1],pixel[2]):
                sortie.putpixel((x,y),(trouver(pixel[0]),0,0))
            else :
                sortie.putpixel((x,y),(255,255,255))
    sortie.save("SAE7/Imageout4.bmp")
print(steganographietrouver("SAE7/Imageout_steg_1.bmp"))



