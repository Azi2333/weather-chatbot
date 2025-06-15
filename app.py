from flask import Flask, request, jsonify
from weather_data import get_weather

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    intent = data['queryResult']['intent']['displayName']
    city = data['queryResult']['parameters'].get('geo-city')

    if not city:
        return jsonify({"fulfillmentText": "Please provide a city name."})

    weather = get_weather(city)

    if "error" in weather:
        return jsonify({"fulfillmentText": weather["error"]})

    if intent == "GetWeather":
        reply = f"The weather in {city} is {weather['temperature']}°C."
    elif intent == "GetHumidity":
        reply = f"The humidity in {city} is {weather['humidity']}%."
    elif intent == "GetWindSpeed":
        reply = f"The wind speed in {city} is {weather['wind_speed']} m/s."
    elif intent == "GetDetails":
        reply = (f"In {city}, the temperature is {weather['temperature']}°C, "
                 f"humidity is {weather['humidity']}%, and wind speed is {weather['wind_speed']} m/s.")
    else:
        reply = "I don't understand that request."

    return jsonify({"fulfillmentText": reply})

if __name__ == "__main__":
    app.run(port=5000)
