import cv2
import numpy


def sketch_face(image):
    width = image.shape[1]
    height = image.shape[0]

    gray0 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.addWeighted(gray0, -1, gray0, 0, 255)
    gray1 = cv2.GaussianBlur(gray1, (11, 11), 0)
    gray2 = numpy.zeros(image.shape[:2], dtype=numpy.float64)

    for y in range(height):
        p0 = gray0[y]
        p1 = gray1[y]
        p = gray2[y]
        for x in range(width):
            tmp0 = p0[x].astype(numpy.int)
            tmp1 = p1[x].astype(numpy.int)
            p[x] = min((tmp0 + (tmp0 * tmp1) / (255 - tmp1)), 255)
    return gray2
