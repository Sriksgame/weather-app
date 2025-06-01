from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'your_openweathermap_api_key'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if data.get('cod') == 200:
                main = data['main']
                weather = data['weather'][0]
                temp = main['temp']
                description = weather['description']

                # Farming Tip Logic
                if 'rain' in description.lower():
                    tip = "🌧️ Rain expected. Avoid sowing or harvesting today."
                elif 'clear' in description.lower():
                    tip = "☀️ Clear sky. Great time for harvesting or irrigation."
                elif 'cloud' in description.lower():
                    tip = "☁️ Cloudy. Monitor soil moisture, consider light irrigation."
                else:
                    tip = "ℹ️ Stay updated. Weather is changing."

                weather_data = {
                    'city': data['name'],
                    'temperature': temp,
                    'description': description,
                    'icon': weather['icon'],
                    'tip': tip
                }
            else:
                weather_data['error'] = "City not found or API issue."

        except Exception as e:
            weather_data['error'] = "Error connecting to weather service."

    return render(request, 'weather/index.html', {'weather_data': weather_data})
