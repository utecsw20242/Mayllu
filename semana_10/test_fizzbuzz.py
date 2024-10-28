from fizzbuzz import fizzbuzz

def test_fizzbuzz_invalid_type():
    assert fizzbuzz("15") == 'Error, el argumento debe ser un número entero'
    assert fizzbuzz(3.5) == 'Error, el argumento debe ser un número entero'
    assert fizzbuzz([3]) == 'Error, el argumento debe ser un número entero'
    assert fizzbuzz(None) == 'Error, el argumento debe ser un número entero'

def test_fizzbuzz_invalid_numbers():
    assert fizzbuzz(0) == 'Error, el número debe ser positivo'
    assert fizzbuzz(-1) == 'Error, el número debe ser positivo'
    assert fizzbuzz(-15) == 'Error, el número debe ser positivo'

def test_fizzbuzz_divisible_by_three():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'

def test_fizzbuzz_divisible_by_five():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(20) == 'Buzz'

def test_fizzbuzz_divisible_by_both():
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz(45) == 'FizzBuzz'

def test_fizzbuzz_not_divisible():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '2'
    assert fizzbuzz(4) == '4'
    assert fizzbuzz(7) == '7'
