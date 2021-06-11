from pymavlink import mavutil
import time
import os

baudrate = 115200

def set_rc_channel_pwm(master, channel_id, pwm=1500):
    if channel_id < 1 or 18 < channel_id:
        print("Channel does not exist.")
        raise ValueError

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    
    rc_channel_values = [65535] * 18
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.
    
    return True

def main():
    # for debugging
    with open("ok.txt", "w+") as file:
        file.write("TUNAPRO1234")

    while not os.path.exists("/dev/ttyACM0"): 
        with open("log.txt", "w+") as file:
            file.write("Waiting for device...\n")
        time.sleep(5)

    master = mavutil.mavlink_connection("/dev/ttyACM0", baud=baudrate)

    with open("log.txt", "w+") as file:
        file.write("Device connected.\n")
    
    delay = 3
    commands = [
        (6, 1400), (6, 1600), 
        (3, 1400), (3, 1600), 
        (5, 1600), (5, 1400),
    ]

    while True:
        for command in commands:
            set_rc_channel_pwm(master, *command)
            time.sleep(delay)
            
if __name__ == "__main__":
    main()
