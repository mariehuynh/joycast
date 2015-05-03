from sys import platform
from subprocess import check_call


def takeSnapshot(rotate180=False):
    """
    Take a picture and return the resulting file. Optionally, rotate the image
    by 180 degrees.
    """
    if platform.startswith('win32'):
        check_call(["CommandCam"])
        imagePath = "image.bmp"
        convertedImagePath = "image.jpg"
    elif platform.startswith('darwin'):
        check_call(["imagesnap"])
        imagePath = "snapshot.jpg"
        convertedImagePath = imagePath
    else:
        raise NotImplementedError("don't know how to take pictures on your OS")

    if rotate180:
        check_call(["convert", imagePath, "-rotate", "180", convertedImagePath])

    return convertedImagePath
