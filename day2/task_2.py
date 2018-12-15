#!/usr/bin/python

from collections import Counter
from difflib import SequenceMatcher
import sys
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def part_1():
	with open('input.dat', 'r') as ids:
		i = 0
		candidates = [0,0]
		for idx in ids:
			letters = Counter()
			for letter in idx:
				letters[letter] += 1
			
			if 2 in letters.values():
				candidates[0] += 1				
			if 3 in letters.values():
				candidates[1] += 1

		print "[+] Found box IDs with two   identical letters: {}".format(candidates[0])
		print "[+] Found box IDs with three identical letters: {}".format(candidates[1])
		print "[+] Final checksum: {}".format(candidates[0] * candidates[1])					

def part_2():
	with open('input.dat', 'r') as ids:
		id_list  = [idx.replace('\n', '') for idx in ids.readlines()]
		candidates = []
		for idx in id_list:
			for idy in id_list:
				if idx <> idy and similar(idx, idy) > 0.96:
					candidates.append(idx)
					candidates.append(idy)
		print "[+] Found correct box IDs : {} ".format(set(candidates))
		sys.stdout.write("[+] Common letters : ")
		for letter in candidates[0]:
			if letter in candidates[1]:
				sys.stdout.write(letter)
		sys.stdout.write("\n")		
		sys.stdout.flush()		

def main():
	part_1()
	part_2()

if __name__ == '__main__':
	main()
