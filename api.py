import requests
import json
import urllib.request 

apiKey = 'c9e521ce9d19eaee59d2bac74f6410a9'

def my_function():
    getCity = input("digite o nome da cidade ")

    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + getCity  + '&APPID=' + apiKey
    req = urllib.request.Request(url)

    ##parsing response
    response = urllib.request.urlopen(req).read()
    cont = json.loads(response.decode('utf-8'))

    print('============PREVISÃO DO TEMPO====================');
    print(cont['name']);
    print(cont['sys']['country']);
    print(cont['weather'][0]['description']);
    print(str (cont['main']['temp_min']) [0:3]);
    print(str (cont['main']['temp_max']) [0:3]);
    print('============FIM PREVISÃO DO TEMPO====================');

my_function()