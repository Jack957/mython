#!/usr/bin/env python
names = ["Amy", "Bob", "Cathy", "David", "Eric"]

for x in names:
	print("Hello " + x)

userName = raw_input("What is your name: ")

if userName:
	print("Hello " + userName);
else:
	print("No name input")
