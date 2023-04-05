import sys
import os
import time

proba=('test', 'proba', 'ojciec','wynik','walic','nie wiem')
sprawdzanie=[]
def koniec(wynik):
    print("Ostateczny wynik:",wynik,"pkt")
    sys.exit(0)
def ilosc():         #tryb do ilosci
    n=len(proba)          
    wynik=0
    x=0
    while x<n:
        slowo=str(input(""))
        m=len(sprawdzanie) 
        for i in range(0, m):
            if(slowo==sprawdzanie[i]):
                print("Powtorzone slowo")
                koniec(wynik)
        
        if slowo in proba:
            wynik+=1
        else:
            print("Zle slowo")
            koniec(wynik)
        sprawdzanie.append(slowo)
        print("Dobre slowo")
        time.sleep(2)
        os.system("cls")
        x+=1
    koniec(wynik)

def na_czas():          #tryb gry na czas
    print("Na czas")
def main():             #glowna funkcja
    wybor=int(input("Wybierz tryb: "))      #zapytanie o wybor
    if(wybor==1):
        ilosc()
    if(wybor==2):
        na_czas()
    if(wybor==3):
        return 0
main()          #wywolanie funckji glownej