from numb3rs import validate 

def test_numb3rs():
    assert validate("1.1.1.1"), "Failed: 1.1.1.1"
    assert not validate("4.12.123.54.7"), "Failed: 4.12.123.54.7"
    assert not validate("900.10.15.60"), "Failed: 900.10.15.60"
    assert not validate("-12.8.12.-80"), "Failed: -12.8.12.-80"
    