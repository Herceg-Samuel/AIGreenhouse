import random

#using shorter names
temp = "Temperature (°C)"
hum = "Humidity (%)"
light = "Light_Intensity (lux)"
moisture = "Soil_Moisture (%)"
CO = "CO₂_Level (ppm)"

#info on watering, giving range
WATERING = {
    "moisture" : range(0, 1),
    "temp" : range(0, 1000),
    "hum" : range(0, 1000)
}

#helper function,loops to check range 
def watering(moisture, temp, hum):
    if(moisture > 0.7):
        print("Skip watering")
    elif((moisture >= 0.35 and moisture <= 0.5) and (temp > 35)):
        print("Light watering")
    elif((moisture < 0.35) and (hum < 0.4) or (temp > 30)):
        print("Watering")
    else:
        print("Invalid")

#info on lighting
LIGHTING = {
    "very_low": range(0, 300),
    "moderate": range(300, 801),
    "high": range(801, 1000),
    "very_high": range(1001, 1000000)
}

#helper function,loops to check range 
def get_light_level(light_value):
    for level, range_values in LIGHTING.items():
        if light_value in range_values:
            return level
    return "invalid"

def shading_control(light_value):
    light_level = get_light_level(light_value)
    match light_level:
        case "very_low":
            print("Open shades")
        case "moderate":
            print("No action")
        case "high":
            print("Close partially")
        case "very_high":
            print("Close fully")
        case _:
            print("Invalid command")


#Defining alert conditions
alert = ["temp > 36", "hum < 0.25", "CO > 1200", "moisture < 0.3", "light > 1100"]   

# Variables to store alert state
consecutive_alerts = 0
current_conditions = 0

def check_condition(condition):
    # Using eval to evaluate the condition string
    try:
        return eval(condition)
    except:
        return False

def check_alerts(temp, hum, CO, moisture, light):
    global consecutive_alerts
    current_conditions = 0
    
    # Check each alert condition
    for condition in alert:
        # Replace variables in condition string with actual values
        condition = condition.replace('temp', str(temp))
        condition = condition.replace('hum', str(hum))
        condition = condition.replace('CO', str(CO))
        condition = condition.replace('moisture', str(moisture))
        condition = condition.replace('light', str(light))
        
        if check_condition(condition):
            current_conditions += 1
    
    # Check if 3 or more conditions are met
    if current_conditions >= 3:
        print("Alert!! Multiple conditions exceeded threshold")
        consecutive_alerts += 1
        if consecutive_alerts >= 2:
            print("CRITICAL RISK FLAG: Alerts triggered for 2 consecutive checks!")
    else:
        # Reset consecutive count if conditions are normal
        consecutive_alerts = 0 
        print("No alert. Back to normal condition.")
        
    return current_conditions


test = [
    [28, 0.45, 800, 0.45, 400],
    [36, 0.20, 1300, 0.25, 1200],
    [38, 0.15, 1400, 0.20, 1300],
    [33, 0.60, 600, 0.75, 200],
    [35, 0.30, 1100, 0.32, 850],
    [31, 0.42, 900, 0.40, 600],
    [37, 0.22, 1250, 0.28, 1150],
    [34, 0.35, 1000, 0.48, 750],
    [38, 0.18, 1350, 0.22, 1250],
    [30, 0.50, 850, 0.55, 500]
]

test_random = list(test) # Create a shallow copy
random.shuffle(test_random)

#allows for the list to be shuffled,then iterates through each
print("--- Calling check_alerts with individual unpacking ---")
for test_data in test_random:
    temp, hum, CO, moisture, light = test_data  # Manual unpacking
    check_alerts(temp, hum, CO, moisture, light)

#AI logging and recomendation
# Initialize logging and tracking variables
moisture_history = []
watering_log = []
MOVING_AVG_WINDOW = 3  # Window size for moving average

def calculate_moving_average(values, window_size):
    if not values:
        return None
    if len(values) < window_size:
        return sum(values) / len(values)
    return sum(values[-window_size:]) / window_size

def recommend_watering_interval(moisture_trend):
    if moisture_trend < 0.3:
        return "Frequent watering needed (Every 6 hours)"
    elif moisture_trend < 0.5:
        return "Regular watering needed (Every 12 hours)"
    elif moisture_trend < 0.7:
        return "Reduced watering needed (Every 24 hours)"
    else:
        return "Minimal watering needed (Monitor and water when moisture drops below 50%)"

# Process and display system decisions for each interval
print("\n=== System Processing Test Scenarios ===")
for i, data in enumerate(test_random):
    temp, hum, CO, moisture_val, light_val = data
    
    # Track moisture history
    moisture_history.append(moisture_val)
    current_moisture_trend = calculate_moving_average(moisture_history, MOVING_AVG_WINDOW)
    
    print(f"\nInterval {i+1}:")
    print(f"Conditions: Temperature={temp}°C, Humidity={hum*100}%, "
          f"CO2={CO}ppm, Moisture={moisture_val*100}%, Light={light_val} lux")
    
    print("System Decisions:")
    print("1. Watering Status:")
    watering(moisture_val, temp, hum)
    
    print("2. Shading Control:")
    shading_control(light_val)
 
    print("3. Alert Status:")
    check_alerts(temp, hum, CO, moisture_val, light_val)
    
    # Log actions and calculate recommendations
    action_log = {
        'interval': i + 1,
        'moisture': moisture_val,
        'temperature': temp,
        'humidity': hum
    }
    watering_log.append(action_log)

# Display trend analysis and recommendations
print("\n=== Moisture Trend Analysis and Recommendations ===")
final_moisture_trend = calculate_moving_average(moisture_history, MOVING_AVG_WINDOW)
print(f"Current Moisture Trend: {final_moisture_trend:.2%}")
print(f"Recommendation: {recommend_watering_interval(final_moisture_trend)}")

# Display action log summary
print("\n=== Action Log Summary ===")
print("Last 5 moisture readings and conditions:")
for log in watering_log[-5:]:
    print(f"Interval {log['interval']}: "
          f"Moisture: {log['moisture']:.2%}, "
          f"Temperature: {log['temperature']}°C, "
          f"Humidity: {log['humidity']:.2%}")   

    
    # Track moisture history
    moisture_history.append(moisture_val)
    current_moisture_trend = calculate_moving_average(moisture_history, MOVING_AVG_WINDOW)

    check_alerts(temp, hum, CO, moisture_val, light_val)
    
    # Log actions and calculate recommendations
    action_log = {
        'interval': i + 1,
        'moisture': moisture_val,
        'temperature': temp,
        'humidity': hum
    }
    watering_log.append(action_log)

# Display trend analysis and recommendations
print("\n=== Moisture Trend Analysis and Recommendations ===")
final_moisture_trend = calculate_moving_average(moisture_history, MOVING_AVG_WINDOW)
print(f"Current Moisture Trend: {final_moisture_trend:.2%}")
print(f"Recommendation: {recommend_watering_interval(final_moisture_trend)}")

