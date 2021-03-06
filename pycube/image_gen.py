import math
from PIL import Image

def genimage(s, cubesize):
    cube_image = Image.new("RGB", (300, 225))
    squaresize = math.floor(75 / cubesize)
    
    rows = [line.strip() for line in s.split("newline")]
    img = [row.split() for row in rows]
    for r in range(len(img) - 1):
        for c in range(len(img[0])):
            if img[r][c] != "empty":
                color = Image.open("../images/" + img[r][c])
                color.thumbnail((squaresize, squaresize), Image.ANTIALIAS)
                cube_image.paste(color, (squaresize * c, squaresize * r))
                
    # Crop image if needed
    cube_image = cube_image.crop((0, 0, 4 * cubesize * squaresize, 3 * cubesize * squaresize))
    return cube_image