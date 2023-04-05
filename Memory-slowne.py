def ilosc():
    print("ilosc")
def na_czas():
    print("Na czas")
def main():
    wybor=int(input("Wybierz tryb: "))
    if(wybor==1):
        ilosc()
    if(wybor==2):
        na_czas()
    if(wybor==3):
        return 0
main()