#Christopher Kenny
#CS 175
#Temperature Conversion Assignment

#Main Function
def main():
  input1 = int(input("Enter '1' to convert Ceclius to Fahrenheit or '2' to convert Fahrenheit to Celcius: "))
  if input1 == 1:
    celcius_to_fahrenheit()
  else:
    fahrenheit_to_celcius()

#Celcius to Fahrenheit Function
def celcius_to_fahrenheit():
  temperature = int(input("Enter temperature in Celcius: "))
  fahrenheit = (temperature * 9/5) + 32
  print(f"{temperature}°C is equal to {fahrenheit}°F")

#Fahrenheit to Celcius Function
def fahrenheit_to_celcius():
  temperature = int(input("Enter temperature in Farhenheit: "))
  celcius = (temperature - 32) * 5/9
  print(f"{temperature}°F is equal to {celcius}°C")

#Print
main()
