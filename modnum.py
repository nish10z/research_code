#! /usr/bin/python3

import argparse

def main(args):
    current_square, num, m, ans = args.b, args.e, args.m, 1
    while num:
        ans = (ans*current_square) % m if num % 2 else ans
        current_square = current_square**2 % m
        num = num//2

    print("{}^{} (mod {}) = {}".format(args.b, args.e, m, ans))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", required=True, type=int, help="The base")
    parser.add_argument("-e", required=True, type=int, help="The exponent")
    parser.add_argument("-m", required=True, type=int, help="The modulus")

    args = parser.parse_args()
    main(args)
