from display.display import draw_arrow, write_text, write_to_terminal
from display.display_helper import get_device
from compass.compass import read_compass, calibrate, read_compass_raw
from push_button.push_button import set_button_callback
import time


compass_calibration =  [[1.013798148849153, 0.032531774503166466, 914.7936953571649], [0.032531774503166466, 1.0766998793747489, 293.5204821723854], [0.0, 0.0, 1.0]]
menu = ["Compass Values", "Compass Arrow"]
menu_curr_location = 0



def main():
    angle = 0
    display = get_device()
    write_to_terminal(display, "Hello welcome to location helper, press use button to see compass values")
    calibrate(compass_calibration)
    set_button_callback(change_menu)

    while True:
        if menu_curr_location == 1:
             draw_arrow(display, read_compass_raw())
             angle = angle + 1
             #print(read_compass_raw())
        elif menu_curr_location == 0:
            values = [menu[menu_curr_location], str(read_compass()), str(read_compass_raw()), " "]
            write_text(display, values, 4, 0, 20)


        #write_text(display, display_text, len(display_text), 0, 20)  
        #angle = (angle + 1) % 360
        #draw_arrow(display, angle)



def change_menu(channel):
    print("pressed")
    global menu_curr_location
    menu_curr_location = (menu_curr_location + 1) % len(menu)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
