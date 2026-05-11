import math

def solution(brown, yellow):
    area = brown + yellow

    for height in range(3, int(math.sqrt(area)) + 1):
        if area % height == 0:
            width = area // height

            if (width - 2) * (height - 2) == yellow:
                return [width, height]