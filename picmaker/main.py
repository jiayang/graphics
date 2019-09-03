class Pixel:

    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b

    def rgb_str(self):
        return f'{self.r} {self.g} {self.b} '

def blank(pixels,w,h):
    '''Fills pixels with a 2d list of pixels according to w and h'''
    for i in range(h):
        pixels.append([])
        for j in range(w):
            pixels[i].append(Pixel())

def to_image(path,pixels,w,h):
    f = open(path,'w')
    f.write(f'P3 {w} {h} 255 ')
    for i in range(h):
        for j in range(w):
            f.write(pixels[i][j].rgb_str())
    f.close()

w = 500
h = 500
pixels = []
blank(pixels,w,h)

#Gradient thing
for r in range(h):
    for c in range(w):
        pixel = pixels[r][c]
        pixel.r = r // 2
        pixel.g = c // 2
        pixel.b = ((r * c) // 2) % 256

to_image('img.ppm', pixels, w, h)
