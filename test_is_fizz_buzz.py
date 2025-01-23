from fizz_buzz import main

def test_3_fizz():
    assert main(3) == [1, 2, "fizz"]
    assert main(6) == [1, 2, "fizz", 4, "buzz", "fizz"]
    assert main(9) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz"]
    assert main(12) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz"]

def test_5_buzz():
    assert main(5) == [1, 2, "fizz", 4, "buzz"]
    assert main(10) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz"]

def test_15_fizz_buzz():
    assert main(15) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]

def test_1_no_fizz_or_buzz():
    assert main(1) == [1]
    assert main(2) == [1, 2]

def test_2_no_fizz_or_buzz():
    assert main(7) == [1, 2, "fizz", 4, "buzz", "fizz", 7]
    assert main(11) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]