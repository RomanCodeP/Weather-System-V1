#You have to install: pip install geopy
import tkinter as tk
import geopy
import requests
import sys
import os
import datetime


############# 
now = datetime.datetime.now()
currenttime = (str(now).split()[1][:2])
#############


#--------------------

def main():
    print("-----------------------------------------")
    print("    Welcome to weather SystemV1")
    print("")
    print("")
    try:
         ubi = input("Please input the location: ")
    except:
         "We had an error finding that location, Try again"
    else:
        os.system("cls")
        #############
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="WeatherTest")
        location = geolocator.geocode(ubi)
        #############
        try:
            Ubicationmeteo = (f"https://api.open-meteo.com/v1/forecast?latitude={float(location.latitude)},&longitude={float(location.longitude)},&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,rain,showers&timezone=auto")
            x = requests.get(Ubicationmeteo)
            w = x.json()
            #############
        except:
            print("We had an error finding that location, Try again")
        else:
            timemeteo = (w["hourly"]["time"][0 + int(currenttime)])
            temperaturemeteo = (w["hourly"]["temperature_2m"][0 + int(currenttime)]) 
            probabilityprecipitationmeteo = (w["hourly"]["precipitation_probability"][0 + int(currenttime)])
            precipitationmeteo = (w["hourly"]["precipitation"][0 + int(currenttime)])
            rainmeteo = (w["hourly"]["rain"][0 + int(currenttime)])
            showersmeteo = (w["hourly"]["showers"][0 + int(currenttime)])

        ############################## night/day detector
            if 6 < int(currenttime) < 18:
                daynight = " ☀️"
            else:
                daynight = " 🌑"
        ##############################

            if 50 < probabilityprecipitationmeteo >= 50:
                probpre = " 🌧️"
            else:
                probpre = " ☀️"
        ##############################


            print("---------------------------------------------------------------------")
            print(f"      The weather in {location} is:")
            print("")
            print(f"Time:   {timemeteo}" + daynight)
            print("")
            print(f"Temperature: {temperaturemeteo}", "°C")
            print("")
            print(f"Probability of precipitation: {probabilityprecipitationmeteo} %" + probpre)
            print("")
            print(f"precipitation: {precipitationmeteo}" + "mm")
            print("")
            print(f"Rain: {rainmeteo}", "mm")
            print("")
            print("---------------------------------------------------------------------")


main()
