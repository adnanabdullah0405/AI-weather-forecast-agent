
# 🌦️ DK Weather Forecast Application

**DK Weather Forecast** is a Streamlit-based web application that provides users with **real-time weather conditions** and **future weather forecasts** for any location. It features **audio feedback** using text-to-speech and **interactive graphs** for enhanced weather visualization.

---

## 📌 Key Features

### 🌍 Current Weather
- Displays **real-time weather** conditions including:
  - Temperature
  - Humidity
  - Wind Speed
  - Atmospheric Pressure
- Input any city/location globally

### 📅 Weather Forecast
- Provides **future weather forecasts** at **3-hour intervals**
- Supports up to **5 future time intervals** for a selected date

### 🔊 Text-to-Speech Integration
- Uses **Google Text-to-Speech (gTTS)** to convert weather data into audio
- Reads:
  - Welcome message
  - Current weather details
  - Forecast summary

### 📈 Interactive Graphs
- Visualizes forecast data:
  - **Temperature**
  - **Humidity**
  - **Wind Speed**
- Built using `matplotlib` for clear and dynamic plotting

---

## 🔧 Technologies Used

| Technology      | Purpose                                 |
|-----------------|------------------------------------------|
| **Streamlit**   | Web app framework (Python)              |
| **gTTS**        | Converts weather data to audio          |
| **OpenWeatherMap API** | Retrieves live and forecasted weather data |
| **Python-dotenv** | Handles secure API key management      |
| **Matplotlib**  | Graphs weather trends visually          |

---

## 📁 Project Structure


