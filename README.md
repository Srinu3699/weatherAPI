
# Weather API

This is a simple weather API built with Flask that fetches weather data for a given location using the OpenWeatherMap API.

## Usage

To use the API, make a GET request to:

```
/weather?location=<CITY>
```

For example: 

```
/weather?location=London
```

This will return a JSON response containing the current weather data for London.

## API Response

The API response will contain weather data including:

- Temperature
- Pressure
- Humidity
- Description
- City name
- Country
- And more...

Example response:

```json
{
  "weather": [
    {
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "main": {
    "temp": 16.18,
    "humidity":87,
  },
  "name": "London",
  "country": "GB"
}
```

## Prerequisites 

- Python 3.x
- Flask
- Requests

## Installation

```bash 
# Install dependencies
pip install -r requirements.txt

#Set OpenWeatherMap API Key 
export OPENWEATHERMAP_API_KEY=<YOUR-API-KEY>

# Run the server
python app.py
```

The server will start on http://localhost:5000

## Credits

This project uses the [OpenWeatherMap](https://openweathermap.org/api) API to fetch weather data.
