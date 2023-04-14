'''
USER MANUAL:
1. OPEN ReRam2, MAXIMIZE IT, CONNECT ALL DEVICES AND SET UP THEM AND ReRam2
2. SET UP THIS SCRIPT: SET CYCLE_NUMBER, CYCLE_DURATION AND OPTIONALLY CURSOR_DELAY AND START_DELAY
3. RUN THIS SCRIPT, RESTORE ReRam2 AND TAKE A BREAK

BENUTZERHANDBUCH:
1. ÖFFNEN SIE ReRam2, MAXIMIEREN ES, SCHLIEßEN ALLE GERÄTE AN UND STELLEN SIE UND ReRam2 EIN
2. STELLEN SIE DIESES SCRIPT EIN: GEBEN CYCLE_NUMBER, CYCLE_DURATION UND OPTIONAL CURSOR_DELAY UND START_DELAY EIN
3. FÜHREN SIE DIESES SCRIPT AUS, STELLEN ReRam2 WIEDER HER UND LEGEN SIE EINE PAUSE EIN
'''


import pyautogui  # pip install pyautogui
import time
from datetime import datetime

'''
    USER PREFERENCES
    
    BENUTZEREINSTELLUNGEN
'''

# Cycle number
CYCLE_NUMBER = 30
# Cycle duration, seconds
CYCLE_DURATION = 60 * 3
# Delay between cursor movements, seconds. If you have a dumb computer, increase this value.
CURSOR_DELAY = 0.1
# Delay befor starting, seconds.
START_DELAY = 5

'''
DO NOT TOUCH THE CODE BELOW IF YOU DO NOT WANT TO CUSTOMIZE SOMETHING

BERÜHREN SIE NICHT DEN KODE UNTEN, WENN SIE NICHT ETWAS ANPASSEN WOLLEN
'''

WH = pyautogui.size()
WIDTH_PROPORTION = WH.width / 1920
HEIGHT_PROPORTION = WH.height / 1080

time.sleep(START_DELAY)

for i in range(CYCLE_NUMBER):
    pyautogui.moveTo(206 * WIDTH_PROPORTION, 95 *
                     HEIGHT_PROPORTION, duration=0.2)  # 'Cyclic Test' tab
    time.sleep(CURSOR_DELAY)
    pyautogui.click()
    time.sleep(CURSOR_DELAY)
    pyautogui.moveTo(72 * WIDTH_PROPORTION, 351 *
                     HEIGHT_PROPORTION, duration=0.2)  # 'Start Cycle' button
    time.sleep(CURSOR_DELAY)
    pyautogui.click()

    print(
        f'New cycle:\n\t>>> {datetime.now().strftime("%d.%m.%Y, %H:%M:%S.%f")}')
    time.sleep(CYCLE_DURATION)

    pyautogui.moveTo(959 * WIDTH_PROPORTION, 654 *
                     HEIGHT_PROPORTION, duration=0.2)  # 'Ok' button
    time.sleep(CURSOR_DELAY)
    pyautogui.click()
    time.sleep(CURSOR_DELAY)
