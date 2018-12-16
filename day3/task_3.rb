#!/usr/local/bin/ruby

def parse_input()
	# extract claims from source file 
	file = File.open('input_3.dat', 'r') {|f| f.read}
	claim_list = file.split("\n")
	claim_list.map!{|claim| claim.split(/[:,#x@ ]/).reject { |c| c.empty? }.map!(&:to_i)}

	claim_list
end

def compute_coordinates(point)
	# return (x.y) coordinates of a point defined by start_point and length
	# system of coordinates is:
	# O -------> x
	# |
	# |
	# |
	# y
	#
	x_a = point[1] 
	y_a = point[2] 
	x_b = x_a
	y_b = y_a + point[4] - 1
	x_c = x_a + point[3] - 1
	y_c = y_b
	x_d = x_c
	y_d = y_a
	
	[point[0], x_a, y_a, x_b, y_b, x_c, y_c, x_d, y_d]
end

def convert_coordinates(claim_list)
	# coverts claims into list of integer coordinates
	# return list of arrays
	claims_conv = Array.new()
	for claim in claim_list
		claims_conv.push(compute_coordinates(claim))
	end

	claims_conv
end

def task_1(claim_list)
	# solver for task 1
	marked = {}
	collisions = 0

	for claim in claim_list
		(claim[1]..claim[7]).step(1) do |inchx|
			(claim[2]..claim[4]).step(1) do |inchy|
				if marked.key?([inchx, inchy])
					marked[[inchx,inchy]] += 1
				else
					marked.store([inchx,inchy], 1)
				end
			end
		end
	end

	marked.each do |key, value|
		if value >= 2
	  	collisions += 1
	  end
	end

	[marked, collisions]  	
end

def task_2(claim_list, claims_marked)
	# solver for task 2
	for claim in claim_list
		area = 0

		(claim[1]..claim[7]).step(1) do |inchx|
			(claim[2]..claim[4]).step(1) do |inchy|
				if claims_marked[[inchx,inchy]] == 1
					area += 1
				end
			end
		end
		if area == (claim[7] - claim[1] + 1) * (claim[4] - claim[2] + 1)
			puts "[+] -{Part 2}- ID of the only claim that doesn't overlap is : %s" % claim[0]
		end
	end
end


if __FILE__ == $0
	claim_list = parse_input()
	puts "[+] Parsed input..."

	claims_conv = convert_coordinates(claim_list)
	puts "[+] -{Part 1}- Converting into coordinates..."

	result_1 = task_1(claims_conv)
	puts "[+] -{Part 1}- Number of collisions is: %s" % result_1[1]

	task_2(claims_conv, result_1[0])
end