def fizzbuzz(n):
    # 1. Validar que la entrada sea un número
    if not isinstance(n, int):
        return 'Error, el argumento debe ser un número entero'

    # 2. Validar que el número sea positivo
    if n <= 0:
        return 'Error, el número debe ser positivo'

    # 3. Lógica del fizzbuzz
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
