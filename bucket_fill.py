""" Coursework 1: Bucket Fill
"""

def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """
    
    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n" 
        
    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


def fill(image, seed_point):
    """ Fill the image from seed point to boundary

    the image should remain unchanged if:
    - the seed_point has a non-integer coordinate
    - the seed_point is on a boundary pixel
    - the seed_point is outside of the image

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel, and
               2 represents a filled pixel
    """

    if not image or not image[0]:
        return image

    if not isinstance(seed_point, tuple) or len(seed_point) != 2:
        return image

    for coord in seed_point:
        if not isinstance(coord, int) or isinstance(coord, bool):
            return image

    row_length = len(image)
    col_length = len(image[0])
    row = seed_point[0]
    col = seed_point[1]

    if row >= row_length or row < 0:
        return image
    if col >= col_length or col < 0:
        return image

    if image[row][col] != 0:
        return image

    filled_image = [pixel_row[:] for pixel_row in image]
    stack = [(row, col)]

    while stack:
        current_row, current_col = stack.pop()

        if current_row < 0 or current_row >= row_length:
            continue
        if current_col < 0 or current_col >= col_length:
            continue
        if filled_image[current_row][current_col] != 0:
            continue

        filled_image[current_row][current_col] = 2

        stack.append((current_row + 1, current_col))
        stack.append((current_row - 1, current_col))
        stack.append((current_row, current_col + 1))
        stack.append((current_row, current_col - 1))

    return filled_image


def example_fill():
    image = load_image("data/bar.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=('hello', 3))

    print("-" * 25)
    print("After filling:")
    show_image(image)


if __name__ == "__main__":
    example_fill()

