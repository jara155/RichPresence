import psutil
from pypresence import Presence
import time
import platform

client_id = "924851988187996190"

RPC = Presence(client_id=client_id)
RPC.connect()

def isRunning(app):
    for i in psutil.process_iter():
        if(app == i.name()):
            return True


while True:

    small_image = ""
    small_text = ""

    RPC.update(
        state = state,
        large_image = "manjaro",
        large_text = platform.release(),
        small_image = small_image,
        small_text = small_text
    )

    time.sleep(30)


