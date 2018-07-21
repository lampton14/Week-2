from PIL import Image
from PIL import ImageFilter


def start():
    print("       How would you like to photoshop?      ")
    print("           1 = invert")
    print("           2 = darken")
    print("           3 = brighten")
    print("          4 = greyscale")
    print("          5 = posterize")
    print("          6 = solarize")
    print("          7 = denoise")
    print("          8 = denoise2")
    print("          9 = denoise3")
    print("            a = blur")
    print("          b = sharpen")
    print("            c = crop")
    return input("                ")
    

def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    new_pixels = []
    for (r, g, b) in pixels:
        new_pixels.append((int(r), int(g), int(b)))
    nim.putdata(new_pixels)
    return nim

def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


'''
During this lab a pixel is a tuple of 3 values (R, G, B)
representing the red, green, and blue components of a color
that each range from [0-255] inclusive. 
The filter functions:
    - take one pixel as an argument,
    - modify the channels of the pixel and
    - return the transformed pixel
'''
def identity(pixel):
    '''
    returns a pixel that is unchanged from the original
    '''
    (r,g,b) = pixel
    return (r,g,b)
    

def invert(pixel):
    '''
    returns a pixel where every pixel channel is 255 minus its value
    '''
    (r,g,b) = pixel
    return (255-r, 255-g, 255-b)

def darken(pixel):
    """
    returns a pixel whose red, green, and blue values are all 90% of those given
    """
    # TODO: students fill this in
    (r,g,b) = pixel
    return (int(.75*r), int(.75*g), int(.75*b))
    
 
def brighten(pixel):
    """
    returns a pixel whose red, green, and blue values are all 110% of those given
    but not over 255 (the maximum value).
    """
    # TODO: students fill this in
    (r,g,b) = pixel
    return (int(1.25*r), int(1.25*g), int(1.25*b))

    
 
def gray_scale(pixel):
    '''
    returns a pixel whose red, green, and blue values are all set to the same value: 
      the average of the original channels 
    '''
    # TODO: students fill this in
    (r,g,b) = pixel
    (r,g,b) = int(r), int(g), int(b)
    r1 = (r+b+g) / 3
    g1 = (r+b+g) / 3
    b1 = (r+b+g) / 3
    return (int(r1), int(g1), int(b1))

    

    
def posterize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - divide channel's range into 4 equal pieces (i.e., 0-63, 64-127, 128-191, 192-255)
     - set the channel's value to a fixed value within that range (i.e., 50, 100, 150, 200)
    """
    # TODO: students fill this in
    (r,g,b) = pixel
    if 0 <= r <= 63:
        r = 50
    if 0 <= g <= 63:
        g = 50
    if 0 <= b <= 63:
        b = 50
    if 64 <= r <= 127:
        r = 100
    if 64 <= g <= 127:
        g = 100
    if 64 <= b <= 127:
        b = 100
    if 128 <= r <= 191:
        r = 150
    if 128 <= g <= 191:
        g = 150
    if 128 <= b <= 191:
        b = 150
    if 192 <= r <= 255:
        r = 200
    if 192 <= g <= 255:
        g = 200
    if 192 <= b <= 255:
        b = 200
        
    return (r, g, b)

    

def solarize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - if the value is less than 128, set it to 255 - the original value.
     - if the value is 128 or greater, don't change it.
    """
    # TODO: students fill this in
    (r,g,b) = pixel
    if r <= 127:
        r = (255 - r)
    if g <= 127:
        g = (255 - g)
    if b <= 127:
        b = (255 - b)
    return (r, g, b)

    

def denoise(pixel):
    '''
    take noise out of a pixel
    '''
    # TODO: students fill this in
    (r,g,b) = pixel
    return (r*10, b*0, g*0)
    

def denoise2(pixel):
    '''
    take noise out of a pixel
    '''
    # TODO: students fill this in
    (r,g,b) = pixel
    return (r*.75, b*20, g*20)
  

def denoise3(pixel):
    '''
    take noise out of a pixel
    '''
    # TODO: Students fill this in
    (r,g,b) = pixel
    if r ==  255 and g == 0 and b == 0:
        return (0,0,0)
    if r == 255 and g == 255 and b == 255:
        return (0,0,0)
    return(r,g,b)
    


def blur(pixel):
    num = int(input("What is your blur power: "))
    original_image = Image.open(input_file)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(num))
    blurred_image.show()
    exit()

def sharpen(pixel):
    num = int(input("What is your sharpen power: "))
    original_image = Image.open(input_file)
    sharpened_image = original_image.filter(ImageFilter.SHARPEN(num))
    sharpened_image.show()
    exit()

    


def crop(pixel):
    start_x = int(input("Enter starting x value:  "))
    start_y = int(input("Enter starting y value:  "))
    end_x = int(input("Enter ending x value:  "))
    end_y = int(input("Enter ending y value:  "))
    img = Image.open(name)
    area = (start_x, start_y, end_x, end_y)
    cropped_img = img.crop(area)
    cropped_img.save("cropped_" + name)
    


def load_and_go(fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    #image.show()
    #nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do
    this you may have to refresh to see it.
    '''
    nimage.save("Dukeproject.png")
    

def main():
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "DUKELOGO2.png"
    mudder = start()
    if mudder == "1":
        load_and_go(input_file, invert)
    elif mudder == "2":
        load_and_go(input_file, darken)
    elif mudder == "3":
        load_and_go(input_file, brighten)
    elif mudder == "4":
        load_and_go(input_file, gray_scale)
    elif mudder == "5":
        load_and_go(input_file, posterize)
    elif mudder == "6":
        load_and_go(input_file, solarize)
    elif mudder == "7":
        load_and_go(input_file, denoise)
    elif mudder == "8":
        load_and_go(input_file, denoise2)
    elif mudder == "9":
        load_and_go(input_file, denoise3)
    elif mudder == "a":
        load_and_go(input_file, blur)
    elif mudder == "b":
        load_and_go(input_file, sharpen)
    elif mudder == "c":
        load_and_go(input_file, crop)
    
main()
while(True):
    if input('continue ?') == "Y":
        main()
    else:
        break
