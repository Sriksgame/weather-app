# weather-app
# 🌦️ Django Weather App for Farmers

A weather forecast web application built using **Django**. Designed especially for farmers, this app allows users to get real-time weather updates, works offline, and is installable on mobile devices as a **Progressive Web App (PWA)**.

---

## 🚀 Features

- 🔍 Search for current weather by city name
- 📱 Installable as a PWA on mobile/desktop
- 💾 Offline support via Service Worker
- 💡 Clean, responsive UI with Bootstrap
- 🌐 OpenWeatherMap API integration

---

## 💻 Technology Stack

| Layer         | Technology                     |
|---------------|--------------------------------|
| Backend       | Django (Python)                |
| Frontend      | HTML, CSS, JavaScript          |
| UI Framework  | Bootstrap 4                    |
| Weather Data  | OpenWeatherMap API             |
| PWA Features  | Manifest + Service Worker      |
| HTTP Client   | `requests` (Python)            |
| Deployment    | Django Development Server      |

---

## 📁 Project Structure

weather_project/
├── weather_app/
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── icons/
│ │ │ ├── icon-192.png
│ │ │ └── icon-512.png
│ │ ├── manifest.json
│ │ └── serviceworker.js
│ ├── templates/
│ │ └── weather/
│ │ └── index.html
│ ├── views.py
│ └── ...
├── staticfiles/ # Created after collectstatic
├── manage.py
└── README.md

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app
Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
bash 
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy
Edit
pip install django requests
🔑 API Setup
This app uses the OpenWeatherMap API.

Sign up at https://openweathermap.org/api

Get your API key

Add it to weather_app/views.py:

python
Copy
Edit
API_KEY = "your_openweathermap_api_key"
🔄 Run Migrations
bash
Copy
Edit
python manage.py migrate
📁 Static Files
Ensure this folder and these files exist:

arduino
Copy
Edit
weather_app/static/css/styles.css
weather_app/static/manifest.json
weather_app/static/serviceworker.js
weather_app/static/icons/icon-192.png
weather_app/static/icons/icon-512.png
Then run:

bash
Copy
Edit
python manage.py collectstatic
▶️ Start the Server
bash
Copy
Edit
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.

📱 PWA Explained
manifest.json: Metadata for installable app (name, icon, theme)

serviceworker.js: Caches assets for offline usage and logs fetch events

📸 Screenshots
Desktop View	Mobile View (PWA)

🧩 To-Do / Future Features
✅ Offline support

✅ Installable on mobile

❌ Weather by location (geolocation support)

❌ 7-day forecast

❌ Multi-language support

📝 License
This project is licensed under the MIT License. Feel free to use and modify it.

🙌 Acknowledgements
OpenWeatherMap

Django

Bootstrap

yaml
Copy
Edit

---

Let me know if you'd like me to also generate the `manifest.json`, `styles.css`, `serviceworker.js`, or `requirements.txt` files for your repo!
