# Funkcija za izracun:
def calculator():
    prvi = input("Molim vas unesite cijeli broj: ")
    drugi = input("Molim vas unesite cijeli drugi broj: ")
    operacija = input("Molim vas unesite operaciju +, -, * ili /")

    if operacija == '+':
        rezultat = int(prvi) + int(drugi)
        print(rezultat)
    elif operacija == '-':
        rezultat = int(prvi) - int(drugi)
        print(rezultat)
    elif operacija == '*':
        rezultat = int(prvi) * int(drugi)
        print(rezultat)
    else:
        rezultat = int(prvi) / int(drugi)
        print(rezultat)
    
    def odlukaPonoviti():
        odluka = input("Želite li napraviti ponovnu kalkulaciju? (y/n)")
        if odluka == 'y':
            calculator()
        elif odluka == 'n':
            exit()
        else:
            print(" Unujeli ste pogrsni znak: " + odluka)
            odlukaPonoviti()

    odlukaPonoviti()
calculator()