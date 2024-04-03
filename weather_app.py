import streamlit as st
import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.weatherapi.com/v1'

    def get_weather(self, location):
        url = f'{self.base_url}/forecast.json?key={self.api_key}&q={location}&days=1&aqi=yes&alerts=yes'
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            st.error(f"Error: {data['error']['message']}")
        else:
            weather = data['current']
            st.markdown(f"### 🌤️ Weather in {location}:")
            st.markdown(f"**Temperature:** {weather['temp_c']}°C")
            st.markdown(f"**Condition:** {weather['condition']['text']}")
            st.markdown(f"**Wind Speed:** {weather['wind_kph']} km/h")
            st.markdown(f"**Humidity:** {weather['humidity']}%")
            
            weather = data['forecast']['forecastday']
            st.markdown(f"### 🪟 Weather Forecast of {location}:")
            st.markdown(f"**Temperature:** {weather[0]['day']['mintemp_c']} to {weather[0]['day']['maxtemp_c']}°C")
            st.markdown(f"**Condition:** {weather[0]['day']['condition']['text']}")
            st.markdown(f"**Wind Speed:** {weather[0]['day']['maxwind_kph']} km/h")
            st.markdown(f"**Humidity:** {weather[0]['day']['avghumidity']}%")

def main():
    st.title("Weather Forecast App")
    st.sidebar.header("Settings")
    
    # API key input
    api_key = st.sidebar.text_input("Enter your WeatherAPI.com API key:")
    
    # WeatherAPI instance
    weather_api = WeatherAPI(api_key)
    
    # Location input
    location = st.text_input("Enter the desired location to get weather information:")
    
    if st.button("Get Weather"):
        if not api_key:
            st.warning("Please enter your API key.")
        elif not location:
            st.warning("Please enter a location.")
        else:
            weather_api.get_weather(location)
# Footer
    st.markdown("""<div style='text-align: center;'><p style='color: #808080;'>&copy; 2024 Paul Joshi Sumith. All rights reserved.</p></div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
