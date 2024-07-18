# calc.py

import argparse

parser = argparse.ArgumentParser(description="CLI CALCULATOR")

subparsers = parser.add_subparsers(help = "sub-command help", dest = "command")

## ADD SUBPARSER: ADDITION
add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

## ADD SUBPARSER: SUBTRACTION
sub = subparsers.add_parser("sub", help = "subtract integers")
sub.add_argument("ints_to_sub", nargs='*', type=int)

def aec_subtract(ints_to_sub):
    if len(ints_to_sub) > 2:
        raise Exception("Sorry, only 2 arguments allowed")

    our_sub = ints_to_sub[0] - ints_to_sub[1]

    if our_sub < 0:
        our_sub = 0

    print(f" the difference of values is: {our_sub}")
    return(our_sub)

## ADD SUBPARSER: MULTIPLICATION
multiply = subparsers.add_parser("multiply", help = "multiply integers")
multiply.add_argument("ints_to_multiply", nargs='*', type=int)

## ADD SUBPARSER: DIVISION
divide = subparsers.add_parser("divide", help = "divide integers")
divide.add_argument("ints_to_divide", nargs='*', type=int)

def aec_divide(ints_to_divide):

    if len(ints_to_divide) > 2:
        raise Exception("Sorry, only 2 arguments allowed")

    if ints_to_divide[1] == 0:
        #print("cannot divide")
        our_div = 0
    else:
        our_div = ints_to_divide[0] /  ints_to_divide[1]
        print(f" the quotient of values is: {our_div}")
    return(our_div)

## WILL ONLY RUN IF BEING RUN FROM CLI
if __name__ == "__main__":

    ## PARSE ARGUMENTS
    args = parser.parse_args()

    ## OUTPUT
    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f" the sum of values is: {our_sum}")

    if args.command == "sub":
        aec_subtract(args.ints_to_sub)

    if args.command == "multiply":
        our_product = args.ints_to_multiply[0]
        for i in range(1, len(args.ints_to_multiply)):
            our_product = our_product * args.ints_to_multiply[i]
        print(f" the product of values is: {our_product}")

    if args.command == "divide":
        aec_divide(args.ints_to_divide)
