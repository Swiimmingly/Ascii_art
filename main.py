from PIL import Image
import argparse




ASCI = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
def main():
    parser = argparse.ArgumentParser(description='Get the image')
    parser.add_argument('--image', metavar='',required=True, type=str,
                        help='image to turn into ascii art')
    parser.add_argument('--invert',action='store_true',
                        help='inverted ascii art')
    args = parser.parse_args()

    im = Image.open(args.image)
    size = (235,178) 
    im = im.resize(size)

    width = im.size[0]
    pixels = list(im.getdata())
    pixels_matrix = []
    end = width
    for i in range(0,len(pixels),width):
        pixels_matrix.append(list(pixels[i:end]))
        end += width

    m = create_art(pixels_matrix,args)
    print_art(m)


def convert(x):
    asc_index = x/4
    pot = x//4
    if pot+0.5 > asc_index:
        asc_index = int(asc_index)
    else:
        asc_index = int(asc_index+1)
    return ASCI[asc_index]

def create_art(pixels_matrix,args):
    for x in range(len(pixels_matrix)):
        for y in range(len(pixels_matrix[x])):
            pixel = pixels_matrix[x][y]
            if args.invert:
                pixels_matrix[x][y] = convert(((255-pixel[0]) + (255 - pixel[1]) + (255 - pixel[2]))/3)
            else:
                pixels_matrix[x][y] = convert((pixel[0]+pixel[1]+pixel[2])/3)
    return pixels_matrix
    
def print_art(pixels_matrix):
    for x in pixels_matrix:
        line = [l+l+l for l in x]
        print(''.join(line))



if __name__ == "__main__":
    main()
    