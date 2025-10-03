'''
PROBLEM: 1  

Write a function string_to_integer_mapping() 
that takes in a string of digits s as a parameter 
and returns a list where each element is the integer value
of the corresponding digit in the string.
'''
def string_to_integer_mapping(s):
    s_list = []
    
    for char in s:
        s_list.append(int(char))

    return s_list

s="12345"
#print(string_to_integer_mapping(s))


'''
PROBLEM: 2

Write a function delete_minimum_elements(nums) that takes in a list of integers nums as a parameter and 
continuously removes the minimum element until the list is empty. The function returns a new list of all 
the elements in nums in the order in which they were removed.
'''

def delete_minimum_elements(nums):
    res = []
    nums.sort()

    while nums:
        res.append(nums[0])
        nums.remove(nums[0])

    return res

nums = [5,3,2,8,3,1]
#print(delete_minimum_elements(nums))

'''
PROBLEM: 3

Write a function longest_common_prefix() that takes in a list of strings 
strings as a parameter.The function returns the longest common prefix 
(not substring) of all strings and if there are none, it returns an empty 
string "".

'''

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for str in strings[1:]:
        while not str.startswith(prefix):

            prefix = prefix[:-1]
            if not prefix:

                return ""
            
    return prefix

#strs = ["internet", "internal", "interval", "interview"]
strs = ["dog", "car", "plane", "ship"]
common_str = longest_common_prefix(strs)
print(common_str)
