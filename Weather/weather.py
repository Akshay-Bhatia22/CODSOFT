from tkinter import *
import requests
import time
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("appid")

def getWeather(root):

    city = textField.get()
    if(city==""):
        messagebox.showwarning(title="Warning!", message="City field cannot be empty")
        return
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    
    json_data = requests.get(api).json()
    # if city not found json data shows key error
    try:
        condition = json_data['weather'][0]['main']
    except KeyError:
        messagebox.showwarning(title="Warning!", message="Invalid city or pincode")
        return
    
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
    
    

root = Tk()
root.geometry("600x500")
root.title("Weather App")


label_title = Label(root, text="Enter the city or pincode to check weather")
label_title.pack()

textField = Entry(root, justify='center', width = 20)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)
get_button = Button(root, text="Get weather", command=lambda: getWeather(root))
get_button.pack()

label1 = Label(root)
label1.pack()
label2 = Label(root)
label2.pack()

root.mainloop()