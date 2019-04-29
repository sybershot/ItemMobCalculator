# ЗДЕСЬ БУДУТ ПОДГРУЖАТЬСЯ СПИСКИ ПРЕДМЕТОВ И МОБОВ, А ЕЩЁ ВСЯКИЕ ПЕРДЕЛКИ ТИПА ГЕНЕРАЦИЯ ПРЕДМЕТОВ/МОБОВ
import random
import json


from pip._vendor.distlib.compat import raw_input

# АЙТЕМСЫ
with open("items.json", "r", encoding='utf-8') as item_in:
    item_l = json.load(item_in)


def gen_item():
    ilvl = float(raw_input("Enter item lvl: "))
    if ilvl > 10:
        ilvl = 10
    elif ilvl == 0:
        ilvl = random.randint(1, 10)
    name = "{} {} {}".format(random.choice(item_l["affix"]), random.choice(item_l["type"]), random.choice(item_l["postfix"]))
    # TODO: stats of items.
    damage = random.uniform(ilvl, ilvl * 2)
    print(name, '\n', int(damage))


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
