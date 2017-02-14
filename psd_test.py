import os, subprocess
os.chdir(os.path.dirname(os.path.realpath(__file__)))
from psd_tools import PSDImage
from PIL import Image



def img_resize(target_width, img):
    w_pct = (target_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(w_pct)))
    return img.resize((target_width, hsize), Image.ANTIALIAS)

psd = PSDImage.load('tee_template.psd')
background = Image.new('RGBA', (1200, 1200), 'white')
shadows = psd.layers[0].layers[0].as_PIL()
shirt = psd.layers[2].layers[4].as_PIL()
subprocess.call(['RScript', 'testPlot.R'])
design = Image.open('test.png')
design = img_resize(1200, design)
design_small = img_resize(200, design)
background.paste(design, (0, 0))
background.paste(shirt, (720, 779), shirt)
background.paste(design_small, (855, 860), design_small)
background.paste(shadows, (720, 780), shadows)
background.save('merged.jpg', format = 'JPEG', quality=100)
subprocess.call(['open', 'merged.jpg'])