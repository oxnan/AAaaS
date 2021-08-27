from PIL import Image
import requests
ASCII_CHARS = "$@B%8&WM#*oahkbdpqzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,      "
ASCII_CHARS = [x for x in ASCII_CHARS]

def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=5):
    initial_pixels = list(image.getdata())
    background = set([ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels[0:10]])
#    if len(background - set(ASCII_CHARS[-10:-1])) == 0:
#        ASCII_CHARS == ASCII_CHARS[::-1]
#        print("ASCII_SET_REVERSED")
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    if len(set(new_pixels)) == 1:
        return
    return ''.join(new_pixels)

def do(image, new_width=100):
    image = resize(image, new_width)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def runner(url, width):
    image = None
    try:
        image = Image.open(requests.get(url, stream=True).raw)
    except Exception:
        print("Unable to find image in",url)
        #print(e)
        return
    image = do(image, int(width))

    # To print on console
    return image 