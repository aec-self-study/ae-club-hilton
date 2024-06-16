####
#  PYTHON EXCERCISES!
####

####
## Loop using while
####

i = 5

while i < 50:
    print(i)
    i = i*2

# loop that loops over the keys in a dictionary and prints the values.
id_lookup = {'Hannah': 5413155, 'KT': 684321655, 'Simon':35413651, 'MACK': 36546354354}

for name in id_lookup:
    print(id_lookup[name])

####
## Write the functions is_odd and is_even that are shown in the lecture
####

def is_odd(x):
    if x%2 != 0:
        r = 'yes'
    else:
        r = 'no'
    return(r)
def is_even(x):
    if x%2 == 0:
        r = 'yes'
    else:
        r = 'no'
    return(r)

is_odd(5)
is_even(5)
is_odd(4)
is_even(4)

####
# Loop over my_first_list and square the value if the value is a number, 
# and print the calories of the fruit if it’s a fruit
####

id_lookup = {'Hannah': 5413155, 'KT': 684321655, 'Simon':35413651, 'MACK': 36546354354}
hilton_list = ['MACK', 4849, 'KT', 719, 'Shivani']
id_lookup.get('test', 0) == 0
for n in hilton_list:
    print(n)
    if isinstance(n, (int, float, complex)) and not isinstance(n, bool):
        print(n**2)
    elif id_lookup.get(n,0) != 0:
        print("id=", id_lookup.get(n))
    else:
        print("neither number nor in dictionary")

####
# Write a function that:
# Takes a dictionary as an argument.
# Loops over the keys in the dictionary.
# Prints the square of the value in the value.
# Hint: use the cal_lookup dictionary for testing.
####

def test_function(dict):
    for k in dict:
        print(dict[k]**.5)

test_function(id_lookup)




