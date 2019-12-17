import urllib
import urllib.request
import json

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

#change this to city = "Dhaka(my city)" or any specific place if you don't want to input it
city = "Dhaka"

#you can Replace with your API KEY
apikey = "de57d237bea6393d152816efaed67e15"

# Puting all the components of the URL together
url = api_endpoint + "?q=" + city + "&appid=" + apikey

response = urllib.request.urlopen(url)
parseResponse = json.loads(response.read())

temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

print (temperature)
print (weather)
