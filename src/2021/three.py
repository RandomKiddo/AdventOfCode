def part_one():
	nums = open('three.txt').read().split('\n')
	zeroes = 0
	ones = 0
	gamma = ''
	epsilon = ''
	for i in range(len(str(nums[0]))):
		for j in nums:
			try:  
				if '0' in (str(j))[i]:
					zeroes += 1
				else:
					ones += 1
			except:
				pass
		if zeroes > ones:
			gamma += '0'
			epsilon += '1'
		else:
			gamma += '1'
			epsilon += '0'
		zeroes = 0
		ones = 0
	gamma_value = int(gamma, 2)
	epsilon_value = int(epsilon, 2)
	print(gamma_value * epsilon_value)

def part_two():
	nums = open('three.txt').read().split('\n')
	zeroes = 0
	ones = 0
	keep_o = nums
	keep_c = nums
	c_rating = 0
	o_rating = 0
	for i in range(len(str(nums[0]))):
		for j in keep_o:
			try:
				if '0' in j[i]:
					zeroes += 1
				else:
					ones += 1
			except:
				pass
		if zeroes > ones:
			keep_o = [_ for _ in keep_o if '0' in _[i]]
		else:
			keep_o = [_ for _ in keep_o if '1' in _[i]]
		if len(keep_o) == 1:
			o_rating = int(keep_o[0], 2)
			break
		zeroes = 0
		ones = 0
	zeroes = 0
	ones = 0
	for i in range(len(str(nums[0]))):
		for j in keep_c:
			try:
				if '0' in j[i]:
					zeroes += 1
				else:
					ones += 1
			except:
				pass
		if zeroes > ones:
			keep_c = [_ for _ in keep_c if '1' in _[i]]
		else:
			keep_c = [_ for _ in keep_c if '0' in _[i]]
		if len(keep_c) == 1:
			c_rating = int(keep_c[0], 2)
			break
		zeroes = 0
		ones = 0
	print(o_rating * c_rating)

part_two()
