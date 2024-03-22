from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather', methods=['POST'])
def weather():
    airport_code = request.form['airport_code']
    api_key = '28d12934e930484a39a155ff51867e13'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={airport_code}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return render_template('weather.html', weather=weather_data)

