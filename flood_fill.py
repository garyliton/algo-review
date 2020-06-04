def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    fill(image, sr, sc, image[sr][sc], newColor)
    return image


def fill(image, sr, sc, og_color, new_color):
    if (sr < 0) or (sr == len(image)) or (sc < 0) or (sc == len(image[0])) or image[sr][sc] != og_color:
        return
    image[sr][sc] = new_color
    fill(image, sr - 1, sc, og_color, new_color)
    fill(image, sr + 1, sc, og_color, new_color)
    fill(image, sr, sc - 1, og_color, new_color)
    fill(image, sr, sc + 1, og_color, new_color)

