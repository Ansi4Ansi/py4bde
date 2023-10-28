from task_Andrey_Simkin_prime import pipeline, is_prime, primes, checksum

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(97) is True
    assert is_prime(293) is True
    assert is_prime(292) is False
    assert is_prime(2339) is True

def test_primes():
    assert len(primes(1000)) == 1000

def test_pipeline():
    test_result = pipeline()
    assert test_result == 7785816
    assert test_result >= 0

def test_checksum():
    test_list = [1, 2, 6, 24]
    assert checksum(test_list) == 6012369

def test_is_prime_complex():
    is_prime_test_list = [2, 3, 5, 7, 11, 13, 17]
    for number in is_prime_test_list:
        assert is_prime(number) == True

test_is_prime()
test_primes()
test_pipeline()
test_checksum()
test_is_prime_complex()