import requests,json
import tkinter as tk
import tkinter.font as tkFont

def fahr(celsius):
    return (9/5)*celsius + 32

def search():
    cityName = cityChoice.get()
    response = requests.get(baseURL + "appid=" + apiKey + "&q=" + cityName)
    weatherModule = response.json()

    if weatherModule['cod'] != '404' and weatherModule['cod'] != '400':
        current = weatherModule["main"]
        currentTemp = current["temp"]
        currentPressure = current["pressure"]
        currentHumidity = current["humidity"]
        desc = weatherModule["weather"][0]["description"]

        city.config(text=f'{cityName}')
        temp.config(text=f'Current Temperature: {(currentTemp - 273.15):.2f} °C / {(fahr(currentTemp - 273.15)):.2f} °F')
        pressure.config(text=f'Current Pressure: {currentPressure}')
        humidity.config(text=f'Current Humidity: {currentHumidity}%')
        description.config(text=f'{desc}')

    else:
        city.config(text=f'{cityName} not found')
        temp.config(text=f'Current Temperature: ')
        pressure.config(text=f'Current Pressure: ')
        humidity.config(text=f'Current Humidity: ')
        description.config(text=f'')

def labelLoading():
    global city, temp, pressure, humidity, description

    city = tk.Label(text=f'Please enter a city name in the field above', fg="white", bg="black")
    city["font"] = font
    city["justify"] = "left"
    city.pack()

    temp = tk.Label(text=f'Current Temperature: ', fg="white", bg="black")
    temp["font"] = font
    temp["justify"] = "left"
    temp.pack()

    pressure = tk.Label(text=f'Current Pressure: ', fg="white", bg="black")
    pressure["font"] = font
    pressure["justify"] = "left"
    pressure.pack()

    humidity = tk.Label(text=f'Current Humidity: ', fg="white", bg="black")
    humidity["font"] = font
    humidity["justify"] = "left"
    humidity.pack()

    description = tk.Label(text=f' ', fg="white", bg="black")
    description["font"] = font
    description["justify"] = "left"
    description.pack()

    apiSource = tk.Label(text='Weather API provided by openweathermap', fg='white', bg='black')
    apiSource.pack()

def main():
    global cityName, cityChoice, apiKey, baseURL, font, searchButton

    apiKey = "2d92543f7cf7d77281a4d0cb549e95e5"
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"

    window = tk.Tk()
    window.title('PyWeather - A Simple Weather App')
    window.geometry("400x400")
    window.configure(bg="black")

    font = tkFont.Font(size=15)

    cityChoice = tk.Entry(window)
    cityChoice.pack()

    searchButton = tk.Button(window, text='Search', command=search)
    searchButton.pack()

    labelLoading()

    window.mainloop()

if __name__ == '__main__':
    main()