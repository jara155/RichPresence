import psutil
from pypresence import Presence
import time
import platform
from colorama import Fore, Back, Style

print(Fore.GREEN + "[+] Vítej")

client_id = "924851988187996190"

print(Fore.GREEN + "[+] Připojuju RPC")
RPC = Presence(client_id=client_id)
RPC.connect()


def isRunning(app):
    for i in psutil.process_iter():
        if(app == i.name()):
            return True


while True:

    small_image = ""
    small_text = ""


    if(isRunning("rocketleague")):
        state = "Hraje si s míčkem."
        small_image = "rl"
        small_text = "Rocket League"

    elif(isRunning("Slapshot.exe")):
        state = "Jezdí po lede."
        small_image = "slapshot"
        small_text = "Slapshot Rebound"

    elif (isRunning("firefox")):
        state = "Brouzdá internetem."
        small_image = "firefox"
        small_text = "Mozilla Firefox"
        details = ""

    else:
        state = "Nudí se..."

    RPC.update(
        state = state,
        large_image = "manjaro",
        large_text = platform.release(),
        small_image = small_image,
        small_text = small_text
    )

    print(Fore.GREEN + "[+] Updatnuto.")

    time.sleep(30)


