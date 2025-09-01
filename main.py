"""
CMPS 6100  Lab 1
Author: Sam Lewis
"""

### the only imports needed are here
import math
import time
###

def is_divisible_by(num, i):
    if num % i == 0:
        return True
    else:
        return False
    # Implement this function


def is_prime(num):
    if num < 2:
            return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True
    # Implement this function
     # remove this line

def generate_primes(upper_bound):
    for num in range(2, upper_bound):
        if is_prime(num):
            print(num) 
    # Implement this function


def count_primes(upper_bound):
    count = 0
    for num in range(2, upper_bound):
        if is_prime(num):
            count += 1
    return count

def generate_twin_primes(upper_bound):
    if upper_bound > 5 and is_prime(3) and is_prime(5):
        print((3, 5))
    if upper_bound > 7 and is_prime(5) and is_prime(7):
        print((5, 7))
    for num in range(1, upper_bound):
        num_1 =  6 * num + 1 
        num_2 =  6 * num - 1
        if num_1 < upper_bound and num_2 > 2 and is_prime(num_1) and is_prime(num_2):
            if (num_2, num_1) not in [(3, 5), (5, 7)]:
                print((num_2, num_1))
    # Implement this function

def count_twin_primes(upper_bound):
    count_2 = 0
    if upper_bound > 5 and is_prime(3) and is_prime(5):
        count_2 += 1
    if upper_bound > 7 and is_prime(5) and is_prime(7):
        count_2 += 1
    for num in range(1, upper_bound):
        num_1 =  6 * num + 1 
        num_2 =  6 * num - 1
        if num_1 < upper_bound and num_2 > 2 and is_prime(num_1) and is_prime(num_2):
            if (num_2, num_1) not in [(3, 5), (5, 7)]:
                count_2 += 1
    return count_2
    # Implement this function
    

#########    #########
### Test Functions ###
#########    #########

# You can run them on the terminal.
# The command:
#
# pytest main.py::test_is_divisible_by
#
# Will run the test_is_divisible_by test function.

def test_is_divisible_by():
    assert is_divisible_by(2, 2) == True
    assert is_divisible_by(3, 2) == False
    assert is_divisible_by(47, 7) == False

def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 241, 461, 701, 881, 883, 997]
    for prime in primes:
        assert is_prime(prime) == True
    composites = [4, 6, 8, 9, 10, 25, 30, 36, 39, 49, 60, 64, 121]
    for composite in composites:
        assert is_prime(composite) == False

def test_count_primes():
    assert count_primes(10) == 4
    assert count_primes(100) == 25
    assert count_primes(1000) == 168
    assert count_primes(10000) == 1229

def test_count_twin_primes():
    assert count_twin_primes(10) == 2
    # The two pairs less than 10 are (3,5) and (5,7)
    assert count_twin_primes(100) == 8
    assert count_twin_primes(1000) == 35
    assert count_twin_primes(10000) == 205
    import time

start = time.time()
generate_twin_primes(10)
end = time.time()

elasped_time_ms = (end - start) * 1000
print("Elapsed Time: {:.2f} milliseconds".format(elasped_time_ms))