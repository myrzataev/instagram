from PIL import Image
import os
size = (1080,1080)
size1 = (100,100)

for j in os.listdir('.'):
    if j.endswith('.jpg'):
        i = Image.open(j)
        logo_img = Image.open('alatoo.jpeg')

        fn, fext = os.path.splitext(j)
        logo_img.thumbnail(size1)
        

        i.thumbnail(size)
        i.paste(logo_img,(970,500))
        i.convert(mode = 'L').save('img/{}_img{}'.format(fn, fext)) 
