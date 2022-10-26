from full_written_numbers.services.full_written_numbers import get_full_written_number


def test_unit_numbers():
    assert get_full_written_number(0) == "zero"
    assert get_full_written_number(1) == "one"
    assert get_full_written_number(2) == "two"
    assert get_full_written_number(3) == "three"
    assert get_full_written_number(4) == "four"
    assert get_full_written_number(5) == "five"
    assert get_full_written_number(6) == "six"
    assert get_full_written_number(7) == "seven"
    assert get_full_written_number(8) == "eight"
    assert get_full_written_number(9) == "nine"


def test_dozens_including_twenty():
    assert get_full_written_number(10) == "ten"
    assert get_full_written_number(11) == "eleven"
    assert get_full_written_number(12) == "twelve"
    assert get_full_written_number(13) == "thirteen"
    assert get_full_written_number(14) == "fourteen"
    assert get_full_written_number(15) == "fifteen"
    assert get_full_written_number(16) == "sixteen"
    assert get_full_written_number(17) == "seventeen"
    assert get_full_written_number(18) == "eighteen"
    assert get_full_written_number(19) == "nineteen"
    assert get_full_written_number(20) == "twenty"


def test_dozens_multiple_of_10():
    assert get_full_written_number(30) == "thirty"
    assert get_full_written_number(40) == "forty"
    assert get_full_written_number(50) == "fifty"
    assert get_full_written_number(60) == "sixty"
    assert get_full_written_number(70) == "seventy"
    assert get_full_written_number(80) == "eighty"
    assert get_full_written_number(90) == "ninety"


def test_several_dozens():
    assert get_full_written_number(37) == "thirty seven"
    assert get_full_written_number(41) == "forty one"
    assert get_full_written_number(48) == "forty eight"
    assert get_full_written_number(52) == "fifty two"

    assert get_full_written_number(66) == "sixty six"
    assert get_full_written_number(73) == "seventy three"
    assert get_full_written_number(84) == "eighty four"
    assert get_full_written_number(95) == "ninety five"
    assert get_full_written_number(99) == "ninety nine"


def test_hundreds():
    assert get_full_written_number(100) == "hundred"
    assert get_full_written_number(101) == "hundred one"
    assert get_full_written_number(110) == "hundred ten"
    assert get_full_written_number(111) == "hundred eleven"
    assert get_full_written_number(112) == "hundred twelve"
    assert get_full_written_number(114) == "hundred fourteen"
    assert get_full_written_number(141) == "hundred forty one"
    assert get_full_written_number(152) == "hundred fifty two"
    assert get_full_written_number(199) == "hundred ninety nine"

    assert get_full_written_number(200) == "two hundred"
    assert get_full_written_number(201) == "two hundred one"
    assert get_full_written_number(210) == "two hundred ten"
    assert get_full_written_number(211) == "two hundred eleven"
    assert get_full_written_number(212) == "two hundred twelve"
    assert get_full_written_number(214) == "two hundred fourteen"
    assert get_full_written_number(241) == "two hundred forty one"
    assert get_full_written_number(252) == "two hundred fifty two"
    assert get_full_written_number(299) == "two hundred ninety nine"


