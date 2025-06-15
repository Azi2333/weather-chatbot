# WeatherBot ☀️

A simple weather chatbot that uses Dialogflow and Python to provide real-time weather updates. Built with Flask, OpenWeatherMap API, and integrated with Telegram using HTTPS via ngrok.

## 💡 Features
- Understands user intents like:
  - "What's the weather in London tomorrow?"
  - "How windy is it in Paris next Friday?"
- Handles missing slot values (like missing city or date) through multi-turn dialogue
- Returns temperature, humidity, wind speed, and other conditions
- Supports Telegram as a front-end interface
- Deployed securely via HTTPS using ngrok / AWS
- 
## 🧠 Core Architecture
- **Dialogflow**: 4 core intents – GetWeather, GetHumidity, GetWindSpeed, GetDetails
- **Flask Webhook**: Receives structured JSON, processes slots, returns weather info
- **OpenWeatherMap API**: External weather source
- **ngrok**: Tunnels local webhook to HTTPS (for testing)
- **Telegram Bot API**: User interface
- **AWS App Runner + Docker + GitHub Actions**: Cloud deployment & auto CI/CD

## ⚙️ How I Built the Bot

- To make this bot, I used **Dialogflow** to create different intents. These intents help the bot understand different ways users ask for weather. My Dialogflow intents handle these variations.
- For the backend, I created two Python files:
  - `app.py`: This acts as the server and connects Dialogflow to the weather service.
  - `weather_data.py`: This file fetches the weather information.
- Since **Telegram** only accepts secure HTTPS connections, I used **ngrok** to convert my local server’s HTTP into HTTPS.
- I also used **Postman** to test the bot and make sure it responds correctly before deploying it.

## 🖼️ Demo

📹 *A detailed explanation video was recorded for this project.*  
👉 https://www.bilibili.com/video/BV1ZkMszuEdw/?spm_id_from=333.1387.upload.video_card.click

## 📚 What I Learned
- How to design Dialogflow intents and entities
- API integration (Telegram + weather API)
- Setting up secure webhooks using ngrok
- Practical experience testing APIs using Postman

