# https://adventofcode.com/2021/day/20

from typing import List, Tuple

# find the value of the pixel by considering the input pixel as the center of the 3x3 tile
def pixelvalue(image: List[List[int]], x: int, y: int, outside_pixel: int = 0) -> int:
    tile_offsets = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]
    output = 0
    for xi, yi in tile_offsets:
        xa, ya = x + xi, y + yi
        pixel = (
            outside_pixel
            if ya < 0 or ya >= len(image) or xa < 0 or xa >= len(image[0])
            else image[ya][xa]
        )
        output = (output << 1) + pixel
    return output


# expand the image by offset on all 4 sides with filler pixel value
def expand(image: List[List[int]], offset: int, filler: int) -> List[List[int]]:
    newX, newY = len(image[0]) + 2 * offset, len(image) + 2 * offset
    newimage = [[filler for _ in range(newX)] for _ in range(newY)]
    for y in range(len(image)):
        for x in range(len(image[0])):
            newimage[y + offset][x + offset] = image[y][x]
    return newimage


# find the filler pixel based on the step and the pixel at 0 and 511 position in the
# image enhancement algorioth. Takes into consideration infinite canvas and
# toggle nature of the process pixels when image_enh_algo[0] = 1 and image_enh_algo[511] = 0
def fillerpixel(image_enh_algo: List[int], step: int) -> int:
    if image_enh_algo[0] == 1:
        if image_enh_algo[511] == 0:
            return 0 if step % 2 == 0 else 1
        else:
            return 0 if step == 0 else 1
    else:
        return 0


# apply the image enhancement algo N times and return the new image
def apply(
    image: List[List[int]], image_enh_algo: List[int], times: int
) -> List[List[int]]:

    for i in range(times):
        filler = fillerpixel(image_enh_algo, i)
        # expand by 1, each step, before we apply the transformation
        image = expand(image, 1, filler)
        # apply transformation for each pixel
        image_output = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        for y in range(len(image)):
            for x in range(len(image[0])):
                image_output[y][x] = image_enh_algo[pixelvalue(image, x, y, filler)]
        image = image_output

    return image


# count the number of light or dark pixel
def countpixels(image: List[List[int]], light: int = 1):
    sum = 0
    for row in image:
        for col in row:
            sum += 1 if col == light else 0
    return sum


def readinput(filename: str) -> Tuple[List[List[int]], List[int]]:
    with open(filename, "rt") as inputFile:
        image_enh_algo = [1 if c == "#" else 0 for c in inputFile.readline().strip()]

        # skip a blank line
        inputFile.readline()

        lines = inputFile.readlines()
        image = []
        for line in lines:
            line = line.strip()
            image.append([1 if c == "#" else 0 for c in line])
        return image, image_enh_algo


def main():
    image, image_enh_algo = readinput("day20.input.txt")
    image_output = apply(image, image_enh_algo, 2)
    count_light_pixel = countpixels(image_output)
    print(f"Number of lit pixels = {count_light_pixel}")


if __name__ == "__main__":
    main()

