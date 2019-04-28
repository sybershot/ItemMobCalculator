# ЗДЕСЬ БУДУТ ПОДГРУЖАТЬСЯ СПИСКИ ПРЕДМЕТОВ И МОБОВ, А ЕЩЁ ВСЯКИЕ ПЕРДЕЛКИ ТИПА ВЫХОДА ИЗ ПРИЛОЖЕНИЯ
# И ГЕНЕРАЦИЯ ПРЕДМЕТОВ/МОБОВ
import random

with open('itemt_list.txt', 'r', encoding='utf-8') as itemt_in:
    itemt_list = itemt_in.read().split('; ')

with open('pfix_list.txt', 'r', encoding='utf-8') as pfix_in:
    pfix_list = pfix_in.read().split('; ')

with open('affix_list.txt', 'r', encoding='utf-8') as affix_in:
    affix_list = affix_in.read().split('; ')


def gen_item(itemt_list, pfix_list, affix_list):
    type = random.choice(itemt_list)
    pfix = random.choice(pfix_list)
    affix = random.choice(affix_list)
    name = affix + ' ' + type + ' ' + pfix
    print(name)


gen_item(itemt_list, pfix_list, affix_list)
