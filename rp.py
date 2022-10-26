import psutil
from pypresence import Presence
import time
import platform
from colorama import Fore

print(Fore.GREEN + "[+] Vítej")

# Insert Client ID (https://support.heateor.com/discord-client-id-discord-client-secret/)
client_id = ""

print(Fore.GREEN + "[+] Připojuju RPC")
RPC = Presence(client_id=client_id)
RPC.connect()
connected = True

def isRunning(app):
    for i in psutil.process_iter():
        if(app == i.name()):
            return True

while True:

    if(isRunning("pycharm.sh") or isRunning("code")):
        RPC.close()
        connected = False
        print(Fore.RED + "[-] Aaaa IDE/Editor je zapnutej, mizím.")
    else:
        RPC.connect()
        connected = True
        print(Fore.GREEN + "[+] Vypadá, že je to pryč, startuju.")


    time.sleep(1.5)

    if(connected):

        small_image = ""
        small_text = ""

        if(isRunning("RocketLeague.ex")):
            state = "Honí se za míčkem."
            small_image = "rl"
            small_text = "Rocket League"

        elif(isRunning("Slapshot.exe")):
            state = "Jezdí po lede ve Slapshotu."
            small_image = "slapshot"
            small_text = "Slapshot Rebound"

        elif(isRunning("RobloxPlayerBet")):
            state = "Tryhardí"
            small_image = "roblox"
            small_text = "Roblox"

        elif(isRunning("WorldOfTanks")):
            state = "Jezdí s tankama"
            small_image = "wot"
            small_text = "WOT"

        # elif (isRunning("firefox")):
        #     state = "Brouzdá internetem."
        #     small_image = "firefox"
        #     small_text = "Mozilla Firefox"
        #     details = ""

        else:
            state = "Nudí se..."

        RPC.update(
            state = state,
            large_image= "endearvour",
            large_text = platform.release(),
            small_image = small_image,
            small_text = small_text
        )

        print(Fore.GREEN + "[+] Updatnuto.")

    time.sleep(30)



