from win10toast import ToastNotifier
import time
import logging

logging.basicConfig()
toaster = ToastNotifier()
waitTime = 60 * 60

print("In {} minutes the first alarm will occur.".format(waitTime / 60))

try:
    while True:
        time.sleep(waitTime)
        toaster.show_toast("HEY", "Time to stand up", duration=10)
        time.sleep(60 * 5)
        toaster.show_toast("Enough", "you can finally sit again", duration=10)
except (KeyboardInterrupt):
    logging.getLogger.debug("SHutdown :(")
