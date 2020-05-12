# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.


def floodFillImage(sr, sc, newColor, image):
    oldColor  = image[sr][sc]
    if sc == 3 or sr == len(image) or sc == -1 or sr == -1:
        return image
    else:
        image[sr][sc] = newColor

    #4 dimention Check
    image = floodFillImage(oldColor, sr-1 , sc, newColor, image)
    image = floodFillImage(oldColor, sr , sc-1, newColor, image)
    image = floodFillImage(oldColor, sr+1 , sc, newColor, image)
    image = floodFillImage(oldColor, sr , sc+1, newColor, image)

    return image

def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    oldColor = image[1][1]
    image = floodFillImage(image, sr, sc, newColor)
    print(image)

if __name__ == "__main__":
    main()
