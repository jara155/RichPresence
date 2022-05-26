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




