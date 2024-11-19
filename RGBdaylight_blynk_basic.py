# @file RGBdaylight_blynk_basic.py
# @brief Blynk RGB Daylight with manual control
# @author Metaphysix
# @version 1.0

import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('YourAuthToken')

# Variables
automode = False
start_time = 0
stop_time = 0
current_time = None

@blynk.VIRTUAL_WRITE(3)
def v3_write_handler(value):
    global automode
    if value == 1:  # Auto mode
        automode = True
        print("Auto mode activated")
    else:  # Manual mode
        automode = False
        print("Manual mode activated")


@blynk.VIRTUAL_WRITE(4)
def v4_time_handler(value):
    global start_time, stop_time
    start_time = value[0]  # start time in seconds
    stop_time = value[1]
    print('Start Time: {}, Stop Time: {}'.format(start_time, stop_time))


def sunrisesim():
    # rgb object
    pass


@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to Blynk")


while True:
    blynk.run()
    if current_time >= start_time and current_time <= stop_time:
        sunrisesim()
