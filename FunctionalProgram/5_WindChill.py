temperature=int(input("Enter the temperature in Fahrenheit: "))
windSpeed=int(input("Enter the wind speed in miles per hour: "))
windchill=0

if temperature>abs(50) or windSpeed>120 or windSpeed<3:
    print("Enter valid temperature and wind speed")
else:
    windchill=35.74+0.6215*temperature+(0.4275*temperature-35.75)*pow(windSpeed,0.16)

print("Windchill is: ",windchill)