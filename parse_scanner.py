#! /usr/bin/env python3

# Import necessary libraries for communication and display use
import drivers
from time import sleep
from datetime import datetime
import sys
import re

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()
display.lcd_clear()
display.lcd_display_string("Grandmas Scanner", 1)

TITLE_REGEX = "StreamTitle='\[\d{2,}\](.*)';"
IDLE_SUBSTR = "StreamTitle='[idle]';"

try:
    buff = ''
    while True:
        buff += sys.stdin.read(1)
        if buff.endswith('\n'):
            line = buff[:-1]
            print(line)
            if IDLE_SUBSTR in line:
                display.lcd_clear()
                display.lcd_display_string("Scanning...", 1)
                print(line)
            else:
                title = re.findall(TITLE_REGEX, line)
                if len(title) > 0:
                    display.lcd_clear()
                    display.lcd_autofit_string(title[0])
                    print(line)
            buff = ''
except KeyboardInterrupt:
    display.lcd_clear()
    display.lcd_display_string("Grandmas Scanner", 1)
except:
   display.lcd_clear()
   display.lcd_display_string("Grandmas Scanner", 1)
   print("Unexpected error:", sys.exc_info()[0])
