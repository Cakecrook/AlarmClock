from playsound import playsound
from time import gmtime, strftime, localtime, sleep

song = "~/Projects/Python/AlarmClock/mySong.mp3"

def main():
    alarm1 = input("Set your alarm for what time? Format: 24 hrs, hh:mm - ")
    alarm2 = input("Set your second alarm for what time? Format: 24 hrs, hh:mm - ")
    print("Alarms set")
    while True:
        if (
            strftime(strftime("%H:%M", localtime())) == alarm1 
            or strftime(strftime("%H:%M", localtime())) == alarm2
        ):
            playsound(song)
        else:
            sleep(25)
        

if __name__ == '__main__':
    main()