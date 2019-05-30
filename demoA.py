import urllib.request
import requests as req
import json
class WeatherData:
    
    temperature = ''
    humid=''
    key = 'bf1b626f3ed6c480088d28d9a053e358'
   
    def __init__(self, city):
        self.city = city
        apiURL='{url}?q={city}&APPID={key}'.format(
        url = 'http://api.openweathermap.org/data/2.5/weather',
        city = self.city,
        key = self.key
        )

        r = req.get(apiURL)
        obj = json.loads(r.text)


        
        self.icon = obj['weather'][0]['icon']
        self.humid = obj['main']['humidity']
    
    
    def getTemperature(self):
        return self.temperature
    def getHumid(self):
        return self.humid
        
    
    
if __name__ == "__main__":
    
    current_weather = WeatherData('Babu,CN')
    print(current_weather.getHumid())
