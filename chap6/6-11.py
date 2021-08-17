cities={
	'new york':{
		'country':'america',
		'population':'8.419 million ',
		'fact':'New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean.',
		},

	'tokyo':{
		'country':'japan',
		'population':'13.96 million',
		'fact':'Tokyo, Japan’s busy capital, mixes the ultramodern and the traditional, from neon-lit skyscrapers to historic temples.',
		},

	'beijing':{
		'country':'china',
		'population':'21.54 million',
		'fact':'Beijing, China’s sprawling capital, has history stretching back 3 millennia.',
		},

	}

for city_name, city_info in cities.items():
	print("\nCity: "+city_name.title())
	print(city_info['country'])
	print(city_info['population'])
	print(city_info['fact'])

