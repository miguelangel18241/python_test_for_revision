hot_weather =  19
cold_weather =  10

weather_today = input('How is the weather today? ')
weather = int(weather_today)

if weather >= hot_weather:
    print ('It is a hot day, drink plenty of water')
elif weather <= cold_weather:
    print ('It is a cold day, Wear warm clothes')
else :
    print ('It is a lovely day.')

is_hot = True
is_cold = False

if is_hot:
    print ('It is a hot day, drink plenty of water')
elif is_cold:
    print ('It is a cold day, Wear warm clothes')
else:
    print ('It is a lovely day.')

print('Enjoy your day!')
