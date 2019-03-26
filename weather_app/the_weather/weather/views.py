from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm

def index(request):

    url ='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=YOUR_API_KEY'
    # city = 'London'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],

        }
        weather_data.append(city_weather)
        print("city_weather>>>",city_weather)

    context = {'city_weather': city_weather,'form':form}
    return render(request,'weather/weather.html',context=context)