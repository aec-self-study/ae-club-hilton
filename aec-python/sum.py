## CLI LESSON
## BUILDING A CLI: COMMAND LINE INTERFACE
## (tool you can interact with)
## If this feels confusing or overwhelming it means you are paying attention!
## oh boy

# building calculator

import argparse

## Set up argument parser
parser = argparse.ArgumentParser(description="Sum two integers.")

## Setting expected number of arguments + expected types
parser.add_argument("ints_to_sum", nargs=2, type=int)

## Parse given arguments
args = parser.parse_args()

## Sum together arguments
our_sum = sum(args.ints_to_sum)

## Print
print(f" the sum of values is: {our_sum}")