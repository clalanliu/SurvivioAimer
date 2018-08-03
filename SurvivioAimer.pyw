import VisualUtils
import keyboard
import pyautogui
import time
import config

def main():
    aimer_turn_on = False
    people_radii = 37

    try:
        while True:
            if keyboard.is_pressed('z'):
                aimer_turn_on = not aimer_turn_on
                print("Turn on?  ", aimer_turn_on)
                time.sleep(0.3)
            if keyboard.is_pressed('o'):
                radii = VisualUtils.getPeopleRadii()
                if radii != None:
                    people_radii = radii
                    print('set people radii: ', people_radii)
            if aimer_turn_on or keyboard.is_pressed('shift'):
                ox, oy = pyautogui.position()
                cx, cy = VisualUtils.getEmimiesPosition([ox, oy], people_radii, config.min_radii, config.max_radii)
                if cx != None:
                    pyautogui.moveTo(cx, cy)
    except KeyboardInterrupt:
        print('Exit!')

if __name__ == '__main__':
    main()