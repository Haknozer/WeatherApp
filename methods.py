from tabulate import tabulate 

weatherDict = {}

def hoursWeather(dailyWeather):
    hours = input("Enter the time to see the weather hourly, otherwise leave blank (Example: 05): ")
    hours = hours + ":00:00"
    print(hours)
    if hours != "":
        for y in dailyWeather["hours"]:
            if hours == y["datetime"]:
                weatherDict[hours] = {
                    "date" : hours,
                    "temp" : str((y["temp"] - 32 )* 5 / 9),
                    "windspeed" : str(y["windspeed"]),
                    "preciptype" : y["preciptype"]
                }
                print("DAILY WEATHER")
                tabulatePrint()

def dailyWeather(weather):
    date = input("Enter date to see weather forecast (Example: 2024-11-08)")
    if date == weather["datetime"]:
        weatherDict[date] = {
            "date" : date,
            "temp" : str((weather["temp"] - 32 )* 5 / 9),
            "windspeed" : str(weather["windspeed"]),
            "preciptype" : weather["preciptype"]
        }
        print("DAILY WEATHER")
        tabulatePrint()


def weeklyWeather(path):
    weatherDict[path["datetime"]] = {
                "date" : path["datetime"],
                "temp" : str((path["temp"] - 32 )* 5 / 9),
                "windspeed": str(path["windspeed"]),
                "preciptype" : path["preciptype"]
            }
    
def tabulatePrint():
    data = [day_data for day_data in weatherDict.values()]
    print(tabulate(data,headers="keys",tablefmt="grid"))
