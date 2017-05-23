import random

prime_numbers = {1, 2, 3, 5, 7, 11, 17, 1, 2, 3, 5}

print("Prime Number =", prime_numbers)

not_a_set = {}
print("Not a set: ", type(not_a_set))

prime_numbers = set()
prime_numbers.add(1)
prime_numbers.add(2)
prime_numbers.add(3)
prime_numbers.add(5)
prime_numbers.add(7)
prime_numbers.add(11)
prime_numbers.add(17)
prime_numbers.add(1)
prime_numbers.add(2)
prime_numbers.add(3)
print("Prime Number =", prime_numbers)

set_a = set()
for i in range(0, 10):
    set_a.add(random.randint(1, 20))
print("Set A = ", set_a)

set_b = set()
for i in range(0, 5):
    set_b.add(random.randint(1, 20))
print("Set B =", set_b)

union = set.union(set_a, set_b)
print("Union =",  union)

diff_a_b = set.difference(set_a, set_b)
print("A diff B =", diff_a_b)

diff_b_a = set.difference(set_b, set_a)
print("B diff A =", diff_b_a)

intersection = set.intersection(set_a, set_b)
print("Intersection = ", intersection)

print("Set A = ", set_a)
for i in range(0, 10):
    rnd = random.randint(1, 20)
    found = rnd in set_a  # Check if an element exists in the Set
    print("{0} => {1}".format(rnd, "Found" if found else "NOT Found"))
