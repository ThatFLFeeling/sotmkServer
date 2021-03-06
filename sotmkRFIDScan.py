from datetime import datetime, timedelta
import time
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522
import threading

def scan():
        while(True):
            id, _ = reader.read()
            print(id)
            currentScan = id

#RFID related variables
reader = SimpleMFRC522()
currentScan = 0
scanThread = threading.Thread(target = scan())
scanThread.start()

#File writing related variables
FILENAME = 'time.txt' #File to be overwritten with current timestamp
now = round(time.time())

#When an RFID is read, write timestamp to file
if (currentScan > 0):
    timestamp_file = open(FILENAME, 'w')
    timestamp_file.write(str(now))
    timestamp_file.close()