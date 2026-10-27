# Fuel Efficiency Calculator

def calculate_efficiency(distance, fuel):
    if distance <= 0:
        return None, "Distance must be greater than zero."

    if fuel <= 0:
        return None, "Fuel consumed must be greater than zero."

    efficiency = distance / fuel
    return efficiency, "Calculation successful."


print("FUEL EFFICIENCY CALCULATOR")
print("--------------------------")

try:
    distance = float(input("Enter distance travelled (km): "))
    fuel = float(input("Enter fuel consumed (litres): "))

    efficiency, message = calculate_efficiency(distance, fuel)

    if efficiency is None:
        print("Error:", message)
    else:
        print("Distance:", distance, "km")
        print("Fuel consumed:", fuel, "litres")
        print("Fuel efficiency:", round(efficiency, 2), "km/L")
        print(message)

except ValueError:
    print("Error: Please enter numbers only.")
