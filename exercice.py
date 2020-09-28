#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))

def generate_prime_numbers(limit):
	prime = []
	nombres = [n for n in range(2, limit + 1)]
	while len(nombres) != 0 :
		prime.append(nombres[0])
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
		# entiers2 = []
		# for elem in entiers:
		# 	if elem % nombres != 0:
		# 		entier2.append(elem)
	return prime

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	#new_str = [elem+n for elem in strings for n in range(num_combinations) if n % excluded_multiples != 0]
	newStr = []
	for i in range(1, num_combinations + 1):
		for elem in strings:
			if excluded_multiples is None or i % excluded_multiples != 0:
				newStr.append(elem + str(i))

	return newStr

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
