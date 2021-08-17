favorite_nums={
	'Lily':[1,2,3],
	'Linda':[2,3],
	'Mike':[3,6],
	'Wendy':[4,9],
	'Zoe':[5,4,3],
	}

for name, nums in favorite_nums.items():
	print("\n"+name.title()+"'s favorite numbers are:")
	for num in nums:
		print(num)