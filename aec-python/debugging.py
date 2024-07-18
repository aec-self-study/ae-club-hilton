import random
 
denoms = list(range(10))
random.shuffle(denoms)
 
for i in range(10):
    ## f-string
    print(f'i: {i}')
    x = denoms[i]
    print(f"x: {x}")
    if x == 0:
        next
    else:
        result = 100 / x
        print(result)



