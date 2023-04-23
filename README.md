# SweaterWeather:
## What it does?: 
SweaterWeather is a web application that allows users to obtain weather information for any location and receive pizza recommendations tailored to the local area.

![github project](https://user-images.githubusercontent.com/29828213/233869261-ea5ffc70-0fc9-4dea-afb2-4a59162becdc.png)


## How to run:
1. Download Depndencies:

    - Download requirements.txt
    - Navigate to the directory containing 'requirements.txt'
    - Run 'pip install -r requirements.txt' to install all the necessary dependencies

2. Get API Keys:

    - Obtain an api key from [weatherapi.com](https://www.weatherapi.com/)
    - Obtain an api key from [google cloud](https://cloud.google.com/apis)

3. Setting API Keys:

    - Open 'app.py' in a text editor
    - Replace 'Enter weatherapi.com API key Here' with your weatherapi.com API key in the line:
      ```
      weather_api_key = 'Enter weatherapi.com API key Here'
      ```
    - Replace 'Enter Google Cloud API Key here' with your Google Cloud API key in the line:
      ```
      weather_api_key = 'Enter weatherapi.com API key Here'
      ```
      
4. Running the application:

    - Run 'app.py' to start the web server
    - Navigate to 'http:/localhost:5000/ in your web browser to access the application

## 
