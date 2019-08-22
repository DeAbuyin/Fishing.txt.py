import os
import random
import time
import progressbar

print("\33[1;37;40m")
portfel = 0
lvl = 0
czas = 10
mnożnik = 10

widgets = [
    progressbar.Bar(), ]

os.system("clear")


def rypka(cena, nazwa, czas, waga):
    global portfel
    global mnożnik
    print("Łowię Rybkę!")
    print("\33[1;36;40m")
    for i in progressbar.progressbar(range(czas), redirect_stdout=True, widgets=widgets):
        time.sleep(0.1)
    os.system("clear")
    (portfel) = (portfel) + cena
    print(
        f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")
    print("\33[1;37;40m")
    print(f"Gartulacje, złowiłeś \33[1;35;40m{nazwa}")
    print(
        f"\33[1;37;40mTa ryba waży \33[1;35;40m{waga} kg\33[1;37;40m, oraz jest warta \33[1;35;40m{cena} Cebul\33[1;37;40m \n")


def main(arg):
    global portfel
    czas = 100
    lvl = 0
    mnożnik = 10
    z = str("2. Mądrze 10 000[C]")
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
    except:
        os.system("clear")
    portfel = float(portfel)
    czas = int(czas)
    lvl = int(lvl)
    mnożnik = int(mnożnik)
    print(
        f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")

    while True:
        #(f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")
        portfel = float(portfel)
        czas = int(czas)
        lvl = int(lvl)
        mnożnik = int(mnożnik)
        print(f"\33[1;34;40m=-=-=-=-=-MENU=-=-=-=-=-\33[1;37;40m\n\
E - aby zacząć łowić \n\
S - aby otworzyć sklep \n\
Clear - aby usunąć zapis \n\
Exit - aby wyjść")

        c = input("")
        if c == 'e':
            os.system("clear")
            rybka = random.randint(0, 100)
            waga = random.randint(1, 10)

            if rybka <= A[0][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)/10
                else:
                    waga = random.randint(5, 10)/10

                nazwa = "Płotkę"

            elif rybka > A[0][lvl] and rybka <= A[1][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 5)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(5, 10)/10
                else:
                    waga = random.randint(10, 20)/10

                nazwa = "Okonia"

            elif rybka > A[1][lvl] and rybka <= A[2][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 12)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(1, 3)
                else:
                    waga = random.randint(3, 5)

                nazwa = "Leszcza"

            elif rybka > A[2][lvl] and rybka <= A[3][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 4)
                else:
                    waga = random.randint(4, 6)

                nazwa = "Pstrąga"

            elif rybka > A[3][lvl] and rybka <= A[4][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 15)/10
                elif waga > 6 and waga <= 9:
                    waga = random.randint(1, 3)
                else:
                    waga = random.randint(3, 6)

                nazwa = "Miętusa"

            elif rybka > A[4][lvl] and rybka <= A[5][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)
                else:
                    waga = random.randint(5, 7)

                nazwa = "Bolenia"

            elif rybka > A[5][lvl] and rybka <= A[6][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 5)
                else:
                    waga = random.randint(5, 10)

                nazwa = "Łososia"

            elif rybka > A[6][lvl] and rybka <= A[7][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 4)
                else:
                    waga = random.randint(5, 10)

                nazwa = "Troć"

            elif rybka > A[7][lvl] and rybka <= A[8][lvl]:
                if waga <= 6:
                    waga = random.randint(1, 2)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 6)
                else:
                    waga = random.randint(5, 11)

                nazwa = "Sandacza"

            else:
                if waga <= 6:
                    waga = random.randint(1, 3)
                elif waga > 6 and waga <= 9:
                    waga = random.randint(2, 10)
                else:
                    waga = random.randint(5, 16)

                nazwa = "Szczupaka"

            cena = waga*mnożnik
            cena = float("%.2f" % round(cena, 2))
            portfel = float("%.2f" % round(portfel, 2))
            rypka(cena, nazwa, czas, waga)

        elif c == 'c':
            portfel = portfel + 100000
            os.system("clear")
            print(
                f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")
        elif c == "exit":
            break

        elif c == "s":
            while True:
                cena_l = 200+100*(lvl)
                cena_u = 10000/czas
                cena_u = int(cena_u)
                q = str("1. Szybsze łowienie")
                d = (f"{q} {cena_u}[C]")
                l = str("3. Przynęta")
                L = (f"{l} {cena_l}[C]")

                k = str("Zakupiono")
                if czas == 10:
                    d = k
                if lvl == 9:
                    L = k
                os.system("clear")
                print(
                    f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: : {mnożnik}\33[1;37;40m")
                print("\33[1;34;40m-=-=-=-=-=SKLEP=-=-=-=-=-\33[1;37;40m")
                print(d)        # Szybsze łowienie
                print(z)        # Mądrze
                print(f"{L}")   # Przynęta
                print(f"4. Lepsze ceny ryb")
                print("Exit")
                sklep = input("Wybierz mądrze: ")

                if sklep == "1" and portfel >= cena_u and d != k and czas > 1:
                    portfel = portfel - cena_u
                    czas = czas - 5
                    print("Dzięki")

                elif sklep == "1" or sklep == "2" or sklep == "3" or sklep == "4" and portfel < cena_u:
                    os.system("clear")
                    print("Jesteś biedakiem!")
                    input()

                elif sklep == "Exit" or sklep == "exit" or sklep == "e":
                    os.system("clear")
                    print(
                        f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")
                    break

                elif sklep == "2" and portfel >= 10000 and z != "O ty śmieszku":
                    portfel = portfel - 10000
                    z = "O ty śmieszku"
                elif sklep == "4" and portfel >= 10*mnożnik:
                    mnożnik = mnożnik + 2
                    portfel = portfel - (mnożnik*10)
                    print("Dzięki!")

                elif sklep == "3" and portfel >= cena_l and L != k:
                    lvl += 1
                    portfel = portfel - cena_l
                    print("Dzięki!")
                portfel = float("%.2f" % round(portfel, 2))
        elif c == "clear" or "Clear":
            portfel = 0
            czas = 100
            mnożnik = 10
            lvl = 0
            os.system("clear")
            print(
                f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")

        else:
            os.system("clear")
            print(
                f"\33[1;33;40mPortfel {portfel}[C]           Prędkość {czas/10}         Poziom przynęty {lvl+1}        Cena za kg: {mnożnik}\33[1;37;40m")
            print(f"Proszę wybrać poprawną opcję!")

        sve = (f"{portfel};{czas};{lvl};{mnożnik}")
        file = open("Save.txt", "w")
        file.write(sve)
        file.close()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
