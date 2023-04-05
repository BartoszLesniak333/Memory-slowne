import sys
import os
import time

proba=('test', 'proba', 'ojciec','wynik','walic','nie wiem')   #probna lista
sprawdzanie=[]
def koniec():
    print("Dziekujemy za granie!")
    sys.exit(0)
def kontyuowanie(wynik):          #koncowa funkcja ma pokazywac wynik
    print("Ostateczny wynik:",wynik,"pkt")
    koniec=str(input("Czy chcesz wyjsc z programu? y/n \n"))
    if(koniec=='n'):
        sys.exit(0)
    if(koniec=='y'):
        main()
def ilosc():         #tryb do ilosci
    n=len(proba)          
    wynik=0
    x=0
    while x<n:
        slowo=str(input(""))
        m=len(sprawdzanie) 
        for i in range(0, m):           #sprawdzanie czy slowo sie nie powtorzylo
            if(slowo==sprawdzanie[i]):
                print("Powtorzone slowo")
                kontyuowanie(wynik)
        
        if slowo in proba:              #dodawanie punktow za dobre slowo
            wynik+=1
        else:                           #konczenie programu 
            print("Zle slowo")
            kontyuowanie(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(2)
        os.system("cls")
        x+=1
    kontyuowanie(wynik)

def na_czas():          #tryb gry na czas
    print("Na czas")
def main():             #glowna funkcja
    wybor=int(input("Wybierz tryb: "))      #zapytanie o wybor
    if(wybor==1):
        ilosc()
    if(wybor==2):
        na_czas()
    if(wybor==3):
        koniec()
main()          #wywolanie funckji glownej