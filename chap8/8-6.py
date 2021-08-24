def city_country(city, country):
    full_name = '"' + city + ", " + country + '"'
    return full_name.title()


n1 = city_country('shanghai', 'china')
print(n1)
n2 = city_country('tokyo', 'japan')
print(n2)
n3 = city_country('london', 'england')
print(n3)
