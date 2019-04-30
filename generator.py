# ЗДЕСЬ БУДУТ ПОДГРУЖАТЬСЯ СПИСКИ ПРЕДМЕТОВ И МОБОВ, А ЕЩЁ ВСЯКИЕ ПЕРДЕЛКИ ТИПА ГЕНЕРАЦИЯ ПРЕДМЕТОВ/МОБОВ
import random
import json

from pip._vendor.distlib.compat import raw_input

# АЙТЕМСЫ
with open("items.json", "r", encoding='utf-8') as item_in:
    item_l = json.load(item_in)


def gen_item():
    try:
        ilvl = float(raw_input("Enter item lvl: "))
    except ValueError:
        ilvl = random.randint(1, 10)
    rarity = random.uniform(0, 3)
    name = ""
    if ilvl > 10:
        ilvl = 10
        # TODO: stats of items.
    if rarity < 1:
        name = random.choice(item_l["type"])
        modifiers = 0
    elif 1 <= rarity < 2:
        name = "{} {}".format(random.choice(item_l["type"]), random.choice(item_l["postfix"]))
        modifiers = 1
    elif 2 <= rarity < 3:
        name = "{} {} {}".format(random.choice(item_l["affix"]), random.choice(item_l["type"]),
                                 random.choice(item_l["postfix"]))
        modifiers = 2
    else:
        name = "{} {} {}".format(random.choice(item_l["affix"]), random.choice(item_l["type"]),
                                 random.choice(item_l["postfix"]))
        modifiers = 3
    damage = random.uniform(ilvl, ilvl * 2)
    print('Name: {}\n Item lvl: {}\n Rarity: {}\n Modifiers: {}\n Damage: {}'
          .format(name, ilvl, rarity, modifiers, int(damage)))


# ======================================================================================================================

# МОБСЫ
with open("mobs.json", "r", encoding='utf-8') as mob_in:
    mob_l = json.load(mob_in)


def gen_mob():
    mtype = random.choice(mob_l["type"])
    pfix = random.choice(mob_l["postfix"])
    affix = random.choice(mob_l["affix"])
    name = affix + ' ' + mtype + ' ' + pfix
    # TODO: stats of mobs.
    print(name)
