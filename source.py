import time
from playsound import playsound
from datetime import datetime

song = "mysong.mp3"

def main():
    localtime = datetime.now().strftime("HH:MM")
    alarm1_time = input("Set your alarm for what time? Format: 24 hrs, hh:mm")
    alarm2_time = input("Set your second alarm for what time? Format: 24 hrs, hh:mm")
    while True:
        if localtime == alarm1_time or localtime == alarm2_time:
            playsound(song)
        else:
            time.sleep(25)
        

if __name__ == '__main__':
    main()