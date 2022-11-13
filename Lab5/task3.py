def get_unique_list_numbers(lev, prav, num) -> list[int]:
    list_numbers = []
    from random import randint
    while len(list_numbers) <= num and num <= len(range(lev, prav)) + 1:
        zn = randint(lev, prav)
        if zn not in list_numbers:
            list_numbers.append(zn)
    return list_numbers
from typing import List
print(get_unique_list_numbers(-10, 10, 15))
