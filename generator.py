# ЗДЕСЬ БУДУТ ПОДГРУЖАТЬСЯ СПИСКИ ПРЕДМЕТОВ И МОБОВ, А ЕЩЁ ВСЯКИЕ ПЕРДЕЛКИ ТИПА ВЫХОДА ИЗ ПРИЛОЖЕНИЯ
# И ГЕНЕРАЦИЯ ПРЕДМЕТОВ/МОБОВ
import random
import json

# АЙТЕМСЫ
with open("items.json", "r", encoding='utf-8') as item_in:
    item_l = json.load(item_in)

def gen_item():
    type = random.choice(item_l["type"])
    pfix = random.choice(item_l["postfix"])
    affix = random.choice(item_l["affix"])
    name = affix + ' ' + type + ' ' + pfix
    print(name)

#=======================================================================================================================

# МОБСЫ
with open("mobs.json", "r", encoding='utf-8') as mob_in:
    mob_l = json.load(mob_in)

def gen_mob():
    type = random.choice(mob_l["type"])
    pfix = random.choice(mob_l["postfix"])
    affix = random.choice(mob_l["affix"])
    name = affix + ' ' + type + ' ' + pfix
    print(name)

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
