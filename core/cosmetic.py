import cv2


def skin_buffing(src, buffing_up=3, detail_up=1, p=0.5):
    dx = buffing_up * 5
    fc = buffing_up * 12.5

    high_pass = cv2.bilateralFilter(src, dx, fc, fc)
    high_pass = (high_pass - src + 127)
    high_pass = cv2.GaussianBlur(high_pass, (2 * detail_up - 1, 2 * detail_up - 1), 0, 0)
    high_pass = src + high_pass * 2 - 1
    high_pass = src * (1 - p) + high_pass * p

    return high_pass
