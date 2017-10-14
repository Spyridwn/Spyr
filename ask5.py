import openaq

city1 = input('Dwse thn prwth polh: ')
city2 = input('Dwse thn deuterh polh: ')

api = openaq.OpenAQ()
status, city1_weather = api.measurements(city = city1)
status, city2_weather = api.measurements(city = city2)

if (city1_weather['results'][0]['value'] > city2_weather['results'][0]['value']):
    print ('H polh ', city1_weather['results'][0]['city'], ' exei ton kalutero aera')
elif (city1_weather['results'][0]['value'] < city2_weather['results'][0]['value']):
    print ('H polh ', city2_weather['results'][0]['city'], ' exei ton kalutero aera')
else:
    print ('Kai oi 2 poleis exoun ton idio aera')
