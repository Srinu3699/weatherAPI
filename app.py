from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
OPENWEATHERMAP_API_KEY = "44c6893f7c2b277c634ff3281f3331a0"
OPENWEATHERMAP_API_URL = "http://api.openweathermap.org/data/2.5/weather"
@app.route('/weather', methods=['GET'])
def get_weather():
    try:
        location = request.args.get('location')
        if not location:
            return jsonify({'error': 'Location not provided'}), 400

        params = {
            'q': location,
            'appid': OPENWEATHERMAP_API_KEY,
            'units': 'metric',
        }

        response = requests.get(OPENWEATHERMAP_API_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to fetch weather data'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
