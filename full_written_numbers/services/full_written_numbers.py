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
    if number < 20:
        second_digit = int(num[-1])
        return f"{teen_prefixes[second_digit]}{TEEN}"
    elif 20 < number < 100:
        first_digit = int(num[0])
        second_digit = int(num[1])
        return f"{ty_prefixes[first_digit]}{TY} {unit_numbers[second_digit] if second_digit > 0 else ''}".strip()
    elif 100 <= number < 1000:
        first_digit = int(num[0])
        rest = int(num[1:])

        hundred_part = f"{'' if first_digit == 1 else unit_numbers[first_digit]} {HUNDRED}".strip()
        dozen_part = get_full_written_number(rest)

        return hundred_part if dozen_part == 'zero' else f"{hundred_part} {dozen_part}"
    elif 1000 <= number < 1_000_000:
        hundred_part = num[-3:] # last three numbers
        thousand_part = num[:-3]

        hundred_sentence_part = get_full_written_number(int(hundred_part))
        thousand_sentence_part = get_full_written_number(int(thousand_part))

        return f"{thousand_sentence_part} {THOUSAND} " \
               f"{hundred_sentence_part if hundred_sentence_part != 'zero' else ''}".strip()




