# PROBLEM 1
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

print(count_mississippi(6))


# PROBLEM 2
def swap_ends(my_str):
    first = my_str[0]
    last = my_str[-1]
    middle = my_str[1:-1]

    return last + middle + first

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# PROBLEM 3
def is_pangram(my_str):
    result = {}
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

    for char in abc:
        result[char] = False

    for char in my_str.lower():
        if char in result.keys():
            result[char] = True

    for val in result.values():
        if val == False:
            return False
        
    return True

#my_str = "The quick brown fox jumps over the lazy dog"
my_str = "The dog jumped"
print(is_pangram(my_str))



