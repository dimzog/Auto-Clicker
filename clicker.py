import time
import cv2
import numpy as np
import pyautogui
import argparse
from datetime import datetime


units = {
    'sec': 1,
    'min': 60,
    'hour': 360
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', type=int, default=10, help='Time to Pause between Submitting', required=False)
    parser.add_argument('--unit', type=str, default='min', help='Unit of Time', required=False)
    args = parser.parse_args()

    unit = args.unit.lower()

    print('Escape by pressing "Ctrl+C".')

    # Calculate sleep interval
    interval = args.interval * units[unit]
    
    # Target Image
    target = cv2.imread('img/target.png')
    width, height = target.shape[:-1]
    
    while True:
        # Take screenshot
        tick = pyautogui.screenshot()

        # Find where Target Img is
        match = cv2.matchTemplate(np.array(tick), target, cv2.TM_CCOEFF_NORMED)
        location = np.where(match >= 0.8)

        if not len(location):
            print('Could not find matching Image, make sure window to be search is visible!')
            break

        # Move Mouse over it, add offset
        y, x = location
        pyautogui.moveTo(x + (height / 2), y + (width / 2))
        
        # Click it
        pyautogui.click(clicks=1)

        print(f'[{datetime.now()}]: Submitted. Sleeping for {interval} min.')

        # Sleep
        time.sleep(interval + 5)
