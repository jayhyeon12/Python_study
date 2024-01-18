# import gift_moule as gm # alias 별칭
from gift_moule import gift, wedding

wedding_note = wedding
# gift_moule.gift(wedding_note, '김일남', 100)
# gm.gift(wedding_note, '김일남', 100)
gift(wedding_note, '김이남', 500)

print(wedding_note)