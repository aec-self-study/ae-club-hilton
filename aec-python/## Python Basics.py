# Setting variable
x = 2
print(x)
print(x**2)

y = "hello!"
print(y)

# Math!
z = x**2 + 5*x
print(z)

# Lists (ordered)
my_fruit_list = ['apple', 1, 'banana', 2]
my_fruit_list[0]

# Dictionaries
id_lookup = {'Hannah': 5413155, 'KT': 684321655, 'Simon':35413651, 'MACK': 36546354354}
id_lookup['MACK']

# Loops!
names = ['Hannah', 'KT', 'Willa', 'Pal', 'Simon', 'MACK', 'Bing', 'Dude', 'Baby Cat']
for n in names:
    print(n)

# Functions
def sq_int(x):
    y = x**2
    return y

sq_int(5)

# Conditions
y = 5
x = 4
def describe_evenness(x):
    if x%2 == 0:
        print("it's even!!!")
    else:
        print("it's odd!!")

describe_evenness(x)
describe_evenness(y)
