import os

locked = False
pwd = ""

file = open('pass.txt', 'r+')

while True:
    if os.stat('pass.txt').st_size == 0: locked = False
    else: locked = True
    file.seek(0)
    pwd = file.read()

    print("u - odblokuj lock, l - zablokuj lock, q - wyjście")
    choice = str(input())
    if choice == "u":
        if locked:
            print("Wprowadz kod do odblokowania")
            chk = input()

            if pwd == chk:
                print("Kod poprawny. Lock odblokowany")
                file.truncate(0)
            else:
                print("Kod niepoprawny. Lock zablokowany")
        else: print("Lock jest obecnie odblokowany")
    elif choice == "l":
        if not locked:
            print("Wprowadz nowy kod aby zablokowac")
            pwd = input()
            file.truncate(0)
            file.write(pwd)
        else: print("Lock jest obecnie zablokowany")
    elif choice == "q":
        break

file.close()


