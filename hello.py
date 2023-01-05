#!/usr/bin/env python
names = ["Amy", "Bob", "Cathy", "David", "Eric"]

for x in names:
	print("Hello " + x)

# raw_input was renamed to input for Python v3.x
userName = input("What is your name: ")

if userName:
	print("Hello " + userName);
else:
	print("No name input")
