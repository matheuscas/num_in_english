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
    assert get_full_written_number(100) == "one hundred"
    assert get_full_written_number(101) == "one hundred one"
    assert get_full_written_number(110) == "one hundred ten"
    assert get_full_written_number(111) == "one hundred eleven"
    assert get_full_written_number(112) == "one hundred twelve"
    assert get_full_written_number(114) == "one hundred fourteen"
    assert get_full_written_number(141) == "one hundred forty one"
    assert get_full_written_number(152) == "one hundred fifty two"
    assert get_full_written_number(199) == "one hundred ninety nine"

    assert get_full_written_number(200) == "two hundred"
    assert get_full_written_number(201) == "two hundred one"
    assert get_full_written_number(210) == "two hundred ten"
    assert get_full_written_number(211) == "two hundred eleven"
    assert get_full_written_number(212) == "two hundred twelve"
    assert get_full_written_number(214) == "two hundred fourteen"
    assert get_full_written_number(241) == "two hundred forty one"
    assert get_full_written_number(252) == "two hundred fifty two"
    assert get_full_written_number(299) == "two hundred ninety nine"

    assert get_full_written_number(999) == "nine hundred ninety nine"


def test_thousands():
    assert get_full_written_number(1000) == "one thousand"
    assert get_full_written_number(1100) == "one thousand one hundred"
    assert get_full_written_number(1110) == "one thousand one hundred ten"
    assert get_full_written_number(1111) == "one thousand one hundred eleven"

    assert get_full_written_number(10000) == "ten thousand"
    assert get_full_written_number(10100) == "ten thousand one hundred"
    assert get_full_written_number(10110) == "ten thousand one hundred ten"
    assert get_full_written_number(10111) == "ten thousand one hundred eleven"

    assert get_full_written_number(100000) == "one hundred thousand"
    assert get_full_written_number(100100) == "one hundred thousand one hundred"
    assert get_full_written_number(100110) == "one hundred thousand one hundred ten"
    assert get_full_written_number(100111) == "one hundred thousand one hundred eleven"

    assert get_full_written_number(300000) == "three hundred thousand"
    assert get_full_written_number(300400) == "three hundred thousand four hundred"
    assert get_full_written_number(300560) == "three hundred thousand five hundred sixty"
    assert get_full_written_number(300891) == "three hundred thousand eight hundred ninety one"

    assert get_full_written_number(999999) == "nine hundred ninety nine thousand nine hundred ninety nine"


def test_millions():
    assert get_full_written_number(999999999) == "nine hundred ninety nine million nine hundred ninety nine " \
                                                 "thousand nine hundred ninety nine"
    assert get_full_written_number(1000000) == "one million"
    assert get_full_written_number(1000100) == "one million one hundred"
    assert get_full_written_number(12345678) == "twelve million three hundred forty five thousand " \
                                                "six hundred seventy eight"


def test_billions():
    assert get_full_written_number(9130848398) == "nine billion one hundred thirty million eight hundred forty eight " \
                                                  "thousand three hundred ninety eight"
    assert get_full_written_number(1000000000) == "one billion"
    assert get_full_written_number(1000000001) == "one billion one"
    assert get_full_written_number(2037741393) == "two billion thirty seven million seven hundred forty one " \
                                                  "thousand three hundred ninety three"



