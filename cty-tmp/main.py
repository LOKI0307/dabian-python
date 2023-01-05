import requests
import random

def metro_city_temp():
    city = random.choice(["delhi","mumbai","bangalore","chennai","pune"])
    #city = input("Enter City:")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=42d9419687a3310cfa68e3c6aaf5951a&units=metric'.format(city)

    res = requests.get(url)
    data = res.json()

    #humidity = data['main']['humidity']
    #pressure = data['main']['pressure']
    #wind = data['wind']['speed']
    #description = data['weather'][0]['description']
    temp = data['main']['temp']
    print("Temperature of {0} is {1} °C".format(city,temp))
#metro_city_temp()
#print('Temperature:',temp,'°C')
#print('Wind:',wind)
#print('Pressure: ',pressure)
#print('Humidity: ',humidity)
#print('Description:',description)
