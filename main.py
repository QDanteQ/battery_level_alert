import winsound
import psutil
import time


def playAlarm():
    winsound.PlaySound("alarm.wav", winsound.SND_ASYNC | winsound.SND_LOOP)


def stopAlarm():
    winsound.PlaySound(None, winsound.SND_PURGE)


def checkBatteryStatus():
    batteryStatus = psutil.sensors_battery()
    return batteryStatus.percent >= 10 or batteryStatus.power_plugged


def main():
    while True:
        if not checkBatteryStatus():
            playAlarm()
            while not checkBatteryStatus():
                time.sleep(0.05)
            stopAlarm()

        time.sleep(30)


if __name__ == '__main__':
    main()
