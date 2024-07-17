import random
 
denoms = list(range(10))
random.shuffle(denoms)

for i in range(10):
  print(f'i: {i}')
  x = denoms[i]
  print(f'denom: {x}')
  try:
    result = 100 / x
  except:
    import pdb; pdb.set_trace()