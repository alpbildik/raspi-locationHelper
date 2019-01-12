import math
import time
import datetime
from .display_helper import get_device, DISPLAY_WIDTH, DISPLAY_HEIGHT
from luma.core.render import canvas
from luma.core.virtual import terminal



def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length) + DISPLAY_WIDTH/2
    dy = int(math.sin(math.radians(angle)) * arm_length) + DISPLAY_HEIGHT/2
    return (dx, dy)


# offset in terms of degree
# smt is wrong with down here +180 makes it right
def draw_arrow(device, offset, radius=32):
    #print(offset)
    with canvas(device) as draw:
        top_point = posn((offset + 90), radius)
        # arctan(0.5) = 0.4636
        # 3/2pi - 2(arctan(0.5)) is the leftest point
        left_point = posn((offset + (270 - 2*26.5650)), radius)
        # symettric of left point
        right_point = posn((offset + (270 + 2*26.5656)), radius)
        bot_point = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        #print (top_point, left_point, right_point)
        draw.polygon(xy=[top_point, left_point, bot_point, right_point], outline="white", fill="white")


# split screen into number of lines
# write lines into screen starting from line_offset
def write_text(device, text_array, number_of_lines, line_offset, row_offset):
    dx = row_offset
    dy = DISPLAY_HEIGHT / number_of_lines 
    with canvas(device) as draw:
        for index, text in enumerate(text_array):
            draw.text((dx,dy * (index + line_offset)), text, fill="white", align="center")
        time.sleep(0.1)


def write_to_terminal(device, text):
    term = terminal(device)
    term.println(text)
    time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
