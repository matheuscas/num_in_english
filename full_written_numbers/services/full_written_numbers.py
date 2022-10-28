from typing import Union, List

unit_numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

special_numbers = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    20: "twenty",
}

TEEN = "teen"
TY = "ty"
HUNDRED = "hundred"
THOUSAND = "thousand"
MILLION = "million"

common_prefixes = {
    3: "thir",
    5: "fif",
    6: "six",
    7: "seven",
    8: "eigh",
    9: "nine",
}

teen_prefixes = {**common_prefixes, **{4: "four"}}
ty_prefixes = {**common_prefixes, **{4: "for"}}


def get_full_written_number(number: int) -> str:
    if number < 10:
        return unit_numbers[number]
    elif number in special_numbers:
        return special_numbers[number]

    num = str(number)

    def get_full_written_number_above_hundred(size: str):
        sizes = {
            HUNDRED: -2,
            THOUSAND: -3,
            MILLION: -6
        }

        first_part = num[sizes[size]:]
        second_part = num[:sizes[size]]

        first_sentence_part = get_full_written_number(int(first_part))
        second_sentence_part = get_full_written_number(int(second_part))

        return f"{second_sentence_part} {size} " \
               f"{first_sentence_part if first_sentence_part != 'zero' else ''}".strip()

    if number < 20:
        second_digit = int(num[-1])
        return f"{teen_prefixes[second_digit]}{TEEN}"
    elif 20 < number < 100:
        first_digit = int(num[0])
        second_digit = int(num[1])
        return f"{ty_prefixes[first_digit]}{TY} {unit_numbers[second_digit] if second_digit > 0 else ''}".strip()
    elif 100 <= number < 1000:
        return get_full_written_number_above_hundred(HUNDRED)
    elif 1000 <= number < 1_000_000:
        return get_full_written_number_above_hundred(THOUSAND)
    elif 1_000_000 <= number < 1_000_000_000:
        return get_full_written_number_above_hundred(MILLION)
