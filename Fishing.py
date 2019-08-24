import os
import random
import time
import progressbar
import platform
# clear musi być na samym dole BO TAK!
print("\33[1;37;40m")
portfel = 0
lvl = 0
czas = 10
mnożnik = 10


def clear_scr():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("NO!")


widgets = [
    progressbar.Bar(), ]

clear_scr()
try:
    file = open("Save.txt", "r")
    svetxt = file.readlines(1)
    file.close()
    text = svetxt[0]
    save = text.split(";")
    lang = save[4]
except:
    lang = "0"

if lang == "0":
    lang = input(f"Wybierz Język/Select language: \n 1.English \n 2.Polski \n")
    clear_scr()
else:
    clear_scr()
lang = lang.lower()

def rypka(cena, nazwa, czas, waga):
    global portfel
    global mnożnik
    if lang == "1" or lang == "en" or lang == "english":
        print("Fishing!")
    else:
        print("Łowię Rybkę!")
    print("\33[1;36;40m")
    for i in progressbar.progressbar(range(czas), redirect_stdout=True, widgets=widgets):
        time.sleep(0.1)
    clear_scr()
    (portfel) = (portfel) + cena
    if lang == "1" or lang == "en" or lang == "english":
        print(
            f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
        print("\33[1;37;40m")
        if nazwa == "a Shoe":
            print(f"CONGRATULATIONS!!!!!! You couth {nazwa} whitch is worth: {cena}[O]")
        else:
            print(f"Congratulations, You caught \33[1;35;40m{nazwa}")
            print(
                f"\33[1;37;40mThis fish weights \33[1;35;40m{waga} kg\33[1;37;40m, and it's worth \33[1;35;40m{cena} Onions\33[1;37;40m \n")
    else:
        print(
            f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
        print("\33[1;37;40m")
        if nazwa == "But":
            print(f"GRATULACJE!!!!!!! złowiłeś {nazwa} który jest warty: {cena}[C]")
        else:
            print(f"Gartulacje, złowiłeś \33[1;35;40m{nazwa}")
            print(
                f"\33[1;37;40mTa ryba waży \33[1;35;40m{waga} kg\33[1;37;40m, oraz jest warta \33[1;35;40m{cena} Cebul\33[1;37;40m \n")


def main(arg):
    global portfel
    global lang
    czas = 100
    lvl = 0
    mnożnik = 10
    A = [[20, 17, 14, 11, 10, 9, 8, 7, 4, 1],  # Płotka
         [35, 31, 27, 23, 20, 17, 14, 11, 7, 3],  # Okoń
         [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],  # Leszcz
         [60, 54, 48, 42, 36, 30, 24, 18, 12, 6],  # Pstrąg
         [70, 65, 60, 55, 50, 45, 40, 35, 30, 25],  # Boleń
         [80, 76, 72, 68, 64, 60, 56, 52, 48, 44],  # Miętus
         [87, 84, 81, 78, 75, 72, 69, 66, 63, 60],  # Łosoś
         [93, 91, 89, 87, 85, 83, 81, 79, 77, 75],  # Troć
         [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]]  # Sandacz i Szcupak

    try:
        file = open("Save.txt", "r")
        svetxt = file.readlines(1)
        file.close()
        text = svetxt[0]
        save = text.split(";")
        portfel = save[0]
        czas = save[1]
        lvl = save[2]
        mnożnik = save[3]
        lang = save[4]
    except:
        clear_scr()
    portfel = float(portfel)
    czas = int(czas)
    lvl = int(lvl)
    mnożnik = int(mnożnik)
    if lang == "1" or lang == "en" or lang == "english":
        print(
            f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
    else:
        print(
            f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")

    while True:
        sve = (f"{portfel};{czas};{lvl};{mnożnik};{lang}")
        file = open("Save.txt", "w")
        file.write(sve)
        file.close()
        portfel = float(portfel)
        czas = int(czas)
        lvl = int(lvl)
        mnożnik = int(mnożnik)
        if lang == "1" or lang == "en" or lang == "english":
            print(f"\33[1;34;40m-=-=-=-=-=MENU=-=-=-=-=-\33[1;37;40m\n\
E - to start fishing \n\
S - to open shop \n\
L - to change language \n\
Clear - to clear your save \n\
Exit - to close the Game")
        else:
            print(f"\33[1;34;40m=-=-=-=-=-MENU=-=-=-=-=-\33[1;37;40m\n\
E - aby zacząć łowić \n\
S - aby otworzyć sklep \n\
L - aby zmienić język \n\
Clear - aby usunąć zapis \n\
Exit - aby wyjść")

        c = input("")
        c = c.lower()
        if c == 'e':
            clear_scr()
            rybka = random.randint(0, 110)
            waga = random.randint(1, 10)

            if rybka <= A[0][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)/10
                else:
                    waga = random.randint(5, 10)/10
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Roach"
                else:
                    nazwa = "Płotkę"

            elif rybka > A[0][lvl] and rybka <= A[1][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 5)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(5, 10)/10
                else:
                    waga = random.randint(10, 20)/10
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Bass"
                else:
                    nazwa = "Okonia"

            elif rybka > A[1][lvl] and rybka <= A[2][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 12)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(1, 3)
                else:
                    waga = random.randint(3, 5)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Bream"
                else:
                    nazwa = "Leszcza"

            elif rybka > A[2][lvl] and rybka <= A[3][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 4)
                else:
                    waga = random.randint(4, 6)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Trout"
                else:
                    nazwa = "Pstrąga"

            elif rybka > A[3][lvl] and rybka <= A[4][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 15)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(1, 3)
                else:
                    waga = random.randint(3, 6)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Burbot"
                else:
                    nazwa = "Miętusa"

            elif rybka > A[4][lvl] and rybka <= A[5][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)
                else:
                    waga = random.randint(5, 7)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "an Asp"
                else:
                    nazwa = "Bolenia"

            elif rybka > A[5][lvl] and rybka <= A[6][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)
                else:
                    waga = random.randint(5, 10)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Salmon"
                    nazwa = "Łososia"

            elif rybka > A[6][lvl] and rybka <= A[7][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 4)
                else:
                    waga = random.randint(5, 10)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Bull-trout"
                else:
                    nazwa = "Troć"

            elif rybka > A[7][lvl] and rybka <= A[8][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 6)
                else:
                    waga = random.randint(5, 11)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Zander"
                else:
                    nazwa = "Sandacza"

            elif rybka >A[8][lvl] and rybka <= 100:
                if waga <= 6:
                    waga = random.randint(1, 3)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 10)
                else:
                    waga = random.randint(5, 16)
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Pike"
                else:
                    nazwa = "Szczupaka"
            else:
                waga = 0
                if lang == "1" or lang == "en" or lang == "english":
                    nazwa = "a Shoe"
                else:
                    nazwa = "But"

            cena = waga*mnożnik
            cena = float("%.2f" % round(cena, 2))
            rypka(cena, nazwa, czas, waga)
            portfel = float("%.2f" % round(portfel, 2))

        elif c == 'c':
            portfel = portfel + 100000
            clear_scr()
            print(
                f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
        elif c == "exit":
            break

        elif c == "s":
            while True:
                cena_l = 200+100*(lvl)
                cena_u = 10000/czas
                cena_u = int(cena_u)
                if lang == "1" or lang == "en" or lang == "english":
                    z = str("2. Wisely 10 000[O]")
                else:
                    z = str("2. Mądrze 10 000[C]")
                if lang == "1" or lang == "en" or lang == "english":
                    q = str("1. Better rod")
                    d = (f"{q} {cena_u}[O]")
                    l = str("3. Better bait")
                    L = (f"{l} {cena_l}[O]")
                    k = str("Sold")
                else:
                    q = str("1. Szybsze łowienie")
                    d = (f"{q} {cena_u}[C]")
                    l = str("3. Przynęta")
                    L = (f"{l} {cena_l}[C]")
                    k = str("Zakupiono")

                if czas == 10:
                    d = k
                if lvl == 9:
                    L = k
                clear_scr()
                if lang == "1" or lang == "en" or lang == "english":
                    print(
                        f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
                    print("\33[1;34;40m-=-=-=-=-=SHOP=-=-=-=-=-\33[1;37;40m")
                else:
                    print(
                        f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: : {mnożnik}\33[1;37;40m")
                    print("\33[1;34;40m-=-=-=-=-=SKLEP=-=-=-=-=-\33[1;37;40m")
                print(d)        # Szybsze łowienie
                print(z)        # Mądrze
                print(f"{L}")   # Przynęta
                if lang == "1" or lang == "en" or lang == "english":
                    print(f"4. Better prices {10*mnożnik}[O]")
                else:
                    print(f"4. Lepsze ceny ryb {10*mnożnik}[C]")
                print("Exit")
                if lang == "1" or lang == "en" or lang == "english":
                    sklep = input("Choose wisely: ")
                else:
                    sklep = input("Wybierz mądrze: ")

                if sklep == "1" and d != k and czas > 1:
                    if portfel < cena_u:
                        if lang == "1" or lang == "en" or lang == "english":
                            print("You are too poor!")
                        else:
                            print("Jesteś biedakiem!")
                    else:
                        portfel = portfel - cena_u
                        czas = czas - 5

                elif sklep == "Exit" or sklep == "exit" or sklep == "e":
                    clear_scr()
                    if lang == "1" or lang == "en" or lang == "english":
                        print(
                            f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
                    else:
                        print(
                            f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
                    break

                elif sklep == "2" and z != "O ty śmieszku" and z != "Oh, You funny Guy":
                    if portfel < 10000:
                        if lang == "1" or lang == "en" or lang == "english":
                            print("You are too poor!")
                        else:
                            print("Jesteś biedakiem!")
                    else:
                        portfel = portfel - 10000
                    if lang == "1" or lang == "en" or lang == "english":
                        z = "Oh, You funny Guy"
                    else:
                        z = "O ty śmieszku"
                elif sklep == "4":
                    if portfel < 10*mnożnik:
                        if lang == "1" or lang == "en" or lang == "english":
                            print("You are too poor!")
                        else:
                            print("Jesteś biedakiem!")
                    else:
                        mnożnik = mnożnik + 1
                        portfel = portfel - (mnożnik*10)

                elif sklep == "3" and L != k:
                    if portfel < cena_l:
                        if lang == "1" or lang == "en" or lang == "english":
                            print("You are too poor!")
                        else:
                            print("Jesteś biedakiem!")
                    else:
                        lvl += 1
                        portfel = portfel - cena_l

                else:
                    clear_scr()
                    if lang == "1" or lang == "en" or lang == "english":
                        print("Please, choose correct option!")
                        input()
                    else:
                        print(f"Proszę wybrać poprawną opcję!")
                        input()
                portfel = float("%.2f" % round(portfel, 2))

        elif c == 'l':
            clear_scr()
            print(f"Wybierz Język/Select language: \n\
1.English \n\
2.Polski")
            lang = input()
            clear_scr()
            if lang == "1" or lang == "en" or lang == "english":
                print(
                    f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
            else:
                print(
                    f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
        elif c == 'clear' or c == 'Clear':
            portfel = 0.0
            czas = 100
            mnożnik = 10
            lvl = 0
            clear_scr()
            if lang == "1" or lang == "en" or lang == "english":
                print(
                    f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
            else:
                print(
                    f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
        else:
            clear_scr()
            if lang == "1" or lang == "en" or lang == "english":
                print(
                    f"\33[1;33;40mWallet {portfel}[O]           Speed {czas/10}         Bait Level {lvl+1}        Price for kg: {mnożnik}[O]\33[1;37;40m")
                print("Please, choose correct option!")
                input()
            else:
                print(
                    f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}[C]\33[1;37;40m")
                print(f"Proszę wybrać poprawną opcję!")
                input()

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
