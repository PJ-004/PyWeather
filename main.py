import requests,json
import tkinter as tk
import tkinter.font as tkFont

def fahr(celsius):
    return (9/5)*celsius + 32

apiKey = "2d92543f7cf7d77281a4d0cb549e95e5"
baseURL = "http://api.openweathermap.org/data/2.5/weather?"

window = tk.Tk()
window.geometry("500x600")
window.configure(bg="black")

font = tkFont.Font(size=23)

cityChoice = tk.Entry(window)
cityName = cityChoice.get()

response = requests.get(baseURL + "appid=" + apiKey + "&q=" + cityName)
weatherModule = response.json()
print(weatherModule)

if weatherModule["cod"] != 404:
    current = weatherModule["main"]
    currentTemp = current["temp"]
    currentPressure = current["pressure"]
    currentHumidity = current["humidity"]
    desc = weatherModule["weather"][0]["description"]

city = tk.Label(text=f'{cityName}', fg="white", bg="black")
city["font"] = font
city["justify"] = "left"
city.pack()

temp = tk.Label(text=f'Current Temperature: {(currentTemp - 273.15):.2f}/{(fahr(currentTemp - 273.15)):.2f}', fg="white", bg="black")
temp["font"] = font
temp["justify"] = "left"
temp.pack()

pressure = tk.Label(text=f'Current Pressure: {currentPressure}', fg="white", bg="black")
pressure["font"] = font
pressure["justify"] = "left"
pressure.pack()

humidity = tk.Label(text=f'Current Humidity: {currentHumidity}%', fg="white", bg="black")
humidity["font"] = font
humidity["justify"] = "left"
humidity.pack()

description = tk.Label(text=f'{desc}', fg="white", bg="black")
description["font"] = font
description["justify"] = "left"
description.pack()

window.mainloop()