import curses
from gpiozero import Robot

robot = Robot(left=(7,8), right=(9,10))
    
actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
}

def main(window):
    next_key = None
    mode_auto = False
    print(mode_auto)
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            print(key, mode_auto)
            if key == 97:
                mode_auto = True
            if key == 109:
                mode_auto = False
                
            if not mode_auto:    
                action = actions.get(key)
                if action is not None:
                    action()
                next_key = key
                while next_key == key:
                    next_key = window.getch()
                # KEY RELEASED
                robot.stop()

curses.wrapper(main)