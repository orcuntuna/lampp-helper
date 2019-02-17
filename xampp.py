#!/usr/bin/env python3

#   @orcuntuna
#   lampp helper script

import sys
import os
import os.path

lampp_adres = "/opt/lampp/"

argumanlar = len(sys.argv)

if(argumanlar > 1):

    komut = sys.argv[1]

    if(komut == "start"):
        os.system("sudo " + lampp_adres + "lampp start") #start
    elif(komut == "stop"):
        os.system("sudo " + lampp_adres + "lampp stop") #stop
    elif(komut == "htdocs"):
        print("htdocs")
    elif(komut == "gui"):
        dosya1 = lampp_adres + "manager-linux-x64.run" #64 bit
        dosya2 = lampp_adres + "manager-linux.run" #32 bit
        if(os.path.isfile(dosya1)):
            os.system("sudo chmod +x " + dosya1) #64 bit chmod
            os.system("sudo " + dosya1) #64 bit open
        elif(os.path.isfile(dosya2)):
            os.system("sudo chmod +x " + dosya2) #32 bit chmod
            os.system("sudo " + dosya2) #32 bit open
        else:
            print("GUI uygulamasina ulasilamiyor")
    elif(komut == "--help"):
        print("""
        -start  :   servisleri aktiflestirir
        -stop   :   servisleri durdurur
        -gui    :   gui uygulamasini calistirir
        """) #help
    else:
        print("hatali parametre")
else:
    print("Parametre gonderilmedi")