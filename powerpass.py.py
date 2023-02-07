#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import re
from sys import exit
from pyfiglet import Figlet


f = Figlet(font='slant')
print(f.renderText('Power Pass'))


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password


def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif not re.search("[a-z]", password):
        return "Weak"
    elif not re.search("[A-Z]", password):
        return "Weak"
    elif not re.search("[0-9]", password):
        return "Weak"
    elif not re.search("[!@#$%^&*()_+=-]", password):
        return "Weak"
    return "Strong"

try:
	length = int(input("Enter the length of the password: "))
	password = generate_password(length)
	strength = check_password_strength(password)
	print(f"Your password:> {password} < Password strength:", strength)
except ValueError:
	print("Please use number")
except KeyboardInterrupt:
    exit()
