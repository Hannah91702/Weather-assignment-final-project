import requests

print("Welcome to Weather Check!")
def GetZip():
  getZip = input("Please enter zip code: ")

  url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=fbc496fefab6da35a0a9e924575e90c2".format(getZip)
  request = requests.get(url) #request data
  weather_details = request.json() #get data in json format

  try:
    show_data(weather_details)
    
  except: #invalid input
    print("Please enter valid zip code. \n\n\n ")
    GetZip() #restart program
  
def Add_location():
  add_location = input("Would you like to check forecast for another location? \n ")
  if add_location == "yes":
    GetZip()
  elif add_location == "no":
    print("Thank you for using Weather Check. Goodbye!")
    return
  
  else: #invalid input
    print("Input is invalid. Please enter 'yes' or 'no'. \n ")
    Add_location()

def show_data(weather_details):
    
    temp = weather_details["main"]["temp"]
    highTemp = weather_details["main"]["temp_max"]
    lowTemp = weather_details["main"]["temp_min"]
    wind_speed = weather_details["wind"]["speed"]
    pressure = weather_details["main"]["pressure"]
    latitude = weather_details["coord"]["lat"]
    longitude = weather_details["coord"]["lon"]
    humid = weather_details["main"]["humidity"]
    weather_description = weather_details["weather"][0]["description"]
    

    print("Current temperature: {} Degree(s) Fahrenheit".format(temp))
    print("Highest temperature: {} Degree(s) Fahrenheit".format(highTemp))
    print("Lowest temperature: {} Degree(s) Fahrenheit".format(lowTemp))
    print("Wind speed: {} Meters A Second".format(wind_speed))
    print("Pressure: {} hecto Pascals".format(pressure))
    print("Latitude: {}".format(latitude))
    print("Longitude: {}".format(longitude))
    print("Humidity: {} Percent".format(humid))
    print("Weather description: {}".format(weather_description))

    Add_location()
    
#run full program
GetZip()
  