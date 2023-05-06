import argparse
import random
import string

parser = argparse.ArgumentParser(description='Genrator a random password.')

parser.add_argument('length',type=int, help='the length of the password')

args = parser.parse_args()

password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=args.length))

print(password)
