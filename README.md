# Weather_forcast
# **DK Weather Forecast Application**
This DK Weather Forecast Application is a Streamlit-based web app that provides users with real-time weather information and weather forecasts. The app allows users to:
View current weather for any location.
Get detailed weather forecasts for a specific date.
Audio playback for the weather data, utilizing Google Text-to-Speech (gTTS).
Interactive graphing of forecast data (temperature, humidity, and wind speed) for better visualization.

# Key Features:
Current Weather: Displays the real-time weather conditions (temperature, humidity, wind speed, and pressure) for any location.
Weather Forecast: Provides weather forecasts for up to 5 future intervals (3-hour intervals) for a specific date.

Text-to-Speech: Converts weather-related information (welcome message, current weather, forecast) into speech using the gTTS (Google Text-to-Speech) library.

Interactive Graphs: Visualizes temperature, humidity, and wind speed forecast data using Matplotlib.

# Technologies Used:
Streamlit: Web framework to build the user interface.

gTTS (Google Text-to-Speech): Converts text to speech for a more interactive experience.

OpenWeatherMap API: Fetches current weather data and weather forecasts.

Python-dotenv: Manages sensitive data (API keys) in a secure .env file.

Matplotlib: Plots weather forecast data.
