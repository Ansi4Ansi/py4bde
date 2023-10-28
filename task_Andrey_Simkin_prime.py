import random
import argparse


def is_prime(x: int) -> bool:
    checking = True
    for element in range(2, x + 1):
        if x % element == 0 and x != element:
            checking = False
            break
        else:
            checking = True
    return checking

def primes(count: int, seed: int) -> list[int]:
    x = 2
    n = 1
    simple_numbers = [2]
    while n != count:
        x += 1
        if is_prime(x) == True:
            simple_numbers.append(x)
            n += 1
    random.seed(seed)
    random.shuffle(simple_numbers)
    return (simple_numbers)

def checksum(counting_list: list[int]) -> int:
    control_sum = 0
    for element in counting_list:
        control_sum += element
        control_sum *= 113
        control_sum = control_sum % 10000007
    return control_sum

def pipeline(seed:int) -> int:
    n = 1000
    # Для проверки чисел на простоту в некотором списке
    prime_checking_list = []
    for i in prime_checking_list:
        is_prime(i)
    # Для генерации списка простых чисел
    counting_list = primes(n, seed)
    # Для подсчета контрольной суммы списка простых чисел
    pipeline_result = checksum(counting_list)
    return pipeline_result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Seed to show')
    parser.add_argument('seed', metavar='N', type=int, nargs='?',
                    help='seed', const=100)
    args = parser.parse_args()
    
    print(pipeline(args.seed))