from generator import *

while True:
    print('1: Generate item\n2: Generate mob\n0: Exit')
    try:
        choice = int(input())
        if choice == 1:
            gen_item()
        elif choice == 2:
            gen_mob()
        elif choice == 0:
            break
    except ValueError:
        print(ValueError)
        print('ENTER CORRECT NUMBER DUMBO')
