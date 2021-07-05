import lodestone
import win32api
import time


while True:
    mavar = lodestone.status("Spriggan")
    if(mavar['Spriggan'] != "unavailable"):
        win32api.MessageBox(0, 'Création Disponible', 'Trouvé')
        break
    print("Création non disponible !")
    time.sleep(30)