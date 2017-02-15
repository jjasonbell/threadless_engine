import os, subprocess
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import numpy as np
from psd_tools import PSDImage
from PIL import Image, ImageEnhance


def img_resize(target_width, img):
    w_pct = (target_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(w_pct)))
    return img.resize((target_width, hsize), Image.ANTIALIAS)

def color_swap(from_triple, to_triple, img):
    data = np.array(img)
    r1, g1, b1 = from_triple
    r2, g2, b2 = to_triple
    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]
    return Image.fromarray(data)

psd = PSDImage.load('tee_template.psd')
background = Image.new('RGBA', (1200, 1200), 'white')
shadows = psd.layers[0].layers[0].as_PIL()
#shadows = ImageEnhance.Brightness(shadows).enhance(0)
shadows = ImageEnhance.Brightness(shadows).enhance(1.1)
shirt = psd.layers[2].layers[4].as_PIL()
subprocess.call(['RScript', 'testPlot.R'])
design = Image.open('test.png')
design = img_resize(1200, design)
design_small = img_resize(200, design)
background.paste(design, (0, 0), design)
background.paste(shirt, (720, 779), shirt)
background.paste(shadows, (720, 780), shadows)
background.paste(design_small, (855, 860), design_small)
background.save('merged.jpg', format = 'JPEG', quality=100)
subprocess.call(['open', 'merged.jpg'])