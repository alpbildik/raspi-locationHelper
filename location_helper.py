from display.display import draw_arrow, write_text
from display.display_helper import get_device

def main():
    angle = 0
    display = get_device()
    write_text(display, ["Hello welcome to", " location helper", "press e to open", "arrow drawer"], 4, 0 , 20)

    while True:
        text = input("")
        if text == "e":
             draw_arrow(display, angle)
             angle = angle + 1
        #write_text(display, display_text, len(display_text), 0, 20)  
        #angle = (angle + 1) % 360
        #draw_arrow(display, angle)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
