#!/usr/bin/python

from itertools import cycle
import bisect

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
      return True
    return False  

def part_1():
	with open('input', 'r') as frequencies:
		freq_list  = [int(freq.replace('\n', '')) for freq in frequencies.readlines()]
		final_freq = 0
		for freq in freq_list:
			final_freq += freq
		print "[+] Final frequency is: {}".format(final_freq)

def part_2():
	freq_list = []
	freq_dup  = 0
	freq_calibrator = []
	
	with open('input', 'r') as frequencies:
		freq_list = [int(freq.replace('\n', '')) for freq in frequencies.readlines()]
		pool = cycle(freq_list)
		
		for freq in pool:
			freq_dup += freq
			if index(freq_calibrator, freq_dup) == False:
				bisect.insort(freq_calibrator, freq_dup)
			else:
				print "[+] Duplicate frequency is: {}".format(freq_dup)
				print "[+] Evaluated {} elements.".format(len(freq_calibrator))
				break

def main():
	part_1()
	part_2()

if __name__ == "__main__":
    main()