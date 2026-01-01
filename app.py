import streamlit as st
import requests
import matplotlib.pyplot as plt
import re
import numpy as np
from datetime import datetime
import os
from dotenv import load_dotenv
from gtts import gTTS
import tempfile

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Set up the page
st.set_page_config(page_title="DK Weather Forecast", page_icon="🌤️")

# Display logo in sidebar
st.sidebar.image("Logo.jpg", use_column_width=True)  # Correct usage
# Updated for the latest Streamlit version

# Sidebar - Features section
st.sidebar.title("Features:")
main_menu_button = st.sidebar.button("Main Menu")
creator_info_button = st.sidebar.button("Creator Info")
feedback_button = st.sidebar.button("Feedback")

# Track the current view
view = "main_menu"

# Show main menu if button clicked
if main_menu_button:
    view = "main_menu"

# Handle the "Creator Info" button to display in the main column
if creator_info_button:
    view = "creator_info"

# Handle the "Feedback" button to show feedback form
if feedback_button:
    view = "feedback"

# Main Content - Based on the view
def text_to_speech(text):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Save the speech to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        tts.save(temp_file.name)
        return temp_file.name

if view == "main_menu":
    # Main Menu
    st.title("🌤️ DK Weather Forecast Application")
    welcome_text = """
        Welcome to the **DK Weather Forecast Application**!
        This application will help you fetch the **current weather** and **weather forecast** for any location you want.
        Simply enter the city name, and we'll provide you with the weather data.
    """
    st.write(welcome_text)

    # Play welcome audio
    audio_file = text_to_speech(welcome_text)
    st.audio(audio_file, format='audio/mp3')

    # User input for city location
    location_input = st.text_input("Enter the city location to check the weather forecast:")

    if location_input:
        # Ask for the date to fetch the forecast
        forecast_date = st.date_input("Select the date for the forecast:")

        # WeatherTool class to interact with OpenWeatherMap API
        class WeatherTool:
            def __init__(self, api_key):
                self.api_key = api_key
                self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"  # Forecast endpoint
                self.base_url = "https://api.openweathermap.org/data/2.5/weather"  # Current weather endpoint

            def get_weather_forecast(self, location):
                params = {
                    'q': location,
                    'appid': self.api_key,
                    'units': 'metric'  # Celsius by default
                }
                response = requests.get(self.forecast_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    forecast_data = []
                    for forecast in data['list']:
                        timestamp = forecast['dt_txt']
                        temp = forecast['main']['temp']
                        humidity = forecast['main']['humidity']
                        wind_speed = forecast['wind']['speed']
                        forecast_data.append({
                            'timestamp': timestamp,
                            'temp': temp,
                            'humidity': humidity,
                            'wind_speed': wind_speed
                        })
                    return forecast_data
                else:
                    return f"Error: Unable to fetch forecast data for {location}. Status code: {response.status_code}"

            def get_current_weather(self, location):
                params = {
                    'q': location,
                    'appid': self.api_key,
                    'units': 'metric'  # Celsius by default
                }
                response = requests.get(self.base_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    weather_description = data['weather'][0]['description']
                    temp = data['main']['temp']
                    humidity = data['main']['humidity']
                    wind_speed = data['wind']['speed']
                    pressure = data['main']['pressure']
                    current_weather_text = f"Current weather in {location}: {weather_description} with {temp}°C temperature, {humidity}% humidity, {wind_speed} m/s wind speed, and {pressure} hPa pressure."
                    return current_weather_text
                else:
                    return f"Error: Unable to fetch current weather data for {location}. Status code: {response.status_code}"

        # Initialize the WeatherTool with OpenWeatherMap API key
        weather_tool = WeatherTool(api_key=API_KEY)  # API key from .env

        # Fetch and display current weather
        current_weather = weather_tool.get_current_weather(location_input)
        st.write(current_weather)

        # Play current weather audio
        audio_file = text_to_speech(current_weather)
        st.audio(audio_file, format='audio/mp3')

        # Fetch and display the weather forecast
        forecast_data = weather_tool.get_weather_forecast(location_input)
        
        if isinstance(forecast_data, list):
            # Filter data for the specified date
            target_date = forecast_date.strftime('%Y-%m-%d')
            filtered_data = [entry for entry in forecast_data if entry['timestamp'].startswith(target_date)]

            if filtered_data:
                # Plot the filtered forecast data using bar plot
                timestamps = [data['timestamp'] for data in filtered_data]
                temps = [data['temp'] for data in filtered_data]
                humidity = [data['humidity'] for data in filtered_data]
                wind_speed = [data['wind_speed'] for data in filtered_data]

                # Bar Plotting for Temperature, Humidity, and Wind Speed
                x = np.arange(len(filtered_data))  # 5 time intervals (next 5 forecast points)

                # Set up the figure and axes
                fig, ax = plt.subplots(figsize=(10, 6))

                # Plot each parameter as a separate bar
                bar_width = 0.25  # Width of each bar
                opacity = 0.8

                rects1 = ax.bar(x - bar_width, temps, bar_width, alpha=opacity, color='b', label='Temperature (°C)')
                rects2 = ax.bar(x, humidity, bar_width, alpha=opacity, color='g', label='Humidity (%)')
                rects3 = ax.bar(x + bar_width, wind_speed, bar_width, alpha=opacity, color='r', label='Wind Speed (m/s)')

                ax.set_xlabel('Time (3-hour intervals)')
                ax.set_ylabel('Values')
                ax.set_title(f'Weather Forecast for {location_input} on {target_date}')
                ax.set_xticks(x)
                ax.set_xticklabels(timestamps, rotation=45, ha='right')
                ax.legend()

                plt.tight_layout()
                st.pyplot(fig)

                # Play the forecast text in audio
                forecast_text = f"Forecast for {location_input} on {target_date}:"
                st.write(forecast_text)
                audio_file = text_to_speech(forecast_text)
                st.audio(audio_file, format="audio/mp3")

            else:
                st.write(f"No forecast data available for {target_date}.")
        else:
            st.write(f"Error: {forecast_data}")
            
# Show Creator Info
elif view == "creator_info":
    creator_info_text = """
        This application of AI Agent is created by **Muhammad Adnan**.
        He is an Electrical Engineering student at **NUST**, and he has a strong passion for **Natural Language Processing (NLP)** and AI Agents.
        This is part of the DK chatbot series, where I am creating some amazing Agents to improve my command on Gen AI.
    """
    st.subheader("Creator Info:")
    st.write(creator_info_text)

    # Play creator info audio
    audio_file = text_to_speech(creator_info_text)
    st.audio(audio_file, format="audio/mp3")

# Show Feedback Form
elif view == "feedback":
    st.subheader("Feedback:")
    feedback = st.text_area("Please leave your feedback here:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")
