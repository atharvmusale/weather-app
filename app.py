
import streamlit as st 
import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title = 'Weather App', page_icon ='🌤️')

st.title('Weather App 🌤️')
st.write('Weather Dekhna Hai? Toh Chalo Dekhte Hai👁️😁')
st.write('Enter the name of the city to get the current weather information. 🌍')

city = st.text_input('Enter city name:')

if st.button('Fetch Weather'):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if(response.status_code == 200):
        st.success('Weather data fetched successfully! ✅')
        data = response.json()
    

        # Extract Weather Information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weathwer_condition = data['weather'][0]['description']
        name = data['name']
        country = data['sys']['country']
        print(data)

        st.subheader(f'{name}, {country}')

        #Create 2rows 2 Columns
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric('Temperature', f'🌡️{temperature}°C')
        col2.metric('Humidity', f'💧{humidity}%')
        col3.metric('Wind Speed', f'💨{wind_speed} m/s')    
        col4.metric('Weather Condition', f'🌤️{weathwer_condition}')
    else:
        st.error('City not found. Please check the city name and try again.')