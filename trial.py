import random
from collections import deque

# --- Configuration ---
NUM_SIMULATION_INTERVALS = 10
MOVING_AVERAGE_WINDOW = 3 # For soil moisture trend analysis

# --- Sensor Data Ranges (for random generation) ---
SENSOR_RANGES = {
    "temperature": (20.0, 40.0),  # °C
    "humidity": (20.0, 90.0),     # %
    "light_intensity": (100.0, 1500.0), # lux
    "soil_moisture": (10.0, 90.0), # %
    "co2_level": (400.0, 1500.0)  # ppm
}

# --- Data Structures ---
class GreenhouseSensorData:
    """Represents sensor readings for a single interval."""
    def __init__(self, temperature, humidity, light_intensity, soil_moisture, co2_level):
        self.temperature = temperature
        self.humidity = humidity
        self.light_intensity = light_intensity
        self.soil_moisture = soil_moisture
        self.co2_level = co2_level

    def __str__(self):
        return (f"Temp: {self.temperature:.1f}°C, Humidity: {self.humidity:.1f}%, "
                f"Light: {self.light_intensity:.1f} lux, Soil Moisture: {self.soil_moisture:.1f}%, "
                f"CO2: {self.co2_level:.1f} ppm")

class GreenhouseDecision:
    """Represents the system's decisions for a single interval."""
    def __init__(self):
        self.watering_action = "No action"
        self.shading_level = "No action"
        self.risk_alert = False
        self.critical_risk_flag = False
        self.alert_details = []

    def __str__(self):
        alert_str = "ALERT!" if self.risk_alert else "No Alert"
        critical_str = "CRITICAL RISK FLAG!" if self.critical_risk_flag else ""
        details = f" ({', '.join(self.alert_details)})" if self.alert_details else ""
        return (f"  - Watering: {self.watering_action}\n"
                f"  - Shading: {self.shading_level}\n"
                f"  - Status: {alert_str}{details} {critical_str}")

# --- Core Logic Functions ---

def generate_sensor_data(interval_num):
    """
    Simulates real-time environmental input.
    Can be random or pre-defined for specific scenarios.
    For this simulation, we use random values within realistic ranges.
    """
    # Example of pre-defined data for specific intervals (uncomment to use)
    # if interval_num == 3:
    #     return GreenhouseSensorData(37, 20, 1200, 25, 1300) # High risk scenario
    # if interval_num == 5:
    #     return GreenhouseSensorData(36, 45, 900, 40, 700) # Light watering, partial shade

    temp = random.uniform(*SENSOR_RANGES["temperature"])
    humid = random.uniform(*SENSOR_RANGES["humidity"])
    light = random.uniform(*SENSOR_RANGES["light_intensity"])
    soil_m = random.uniform(*SENSOR_RANGES["soil_moisture"])
    co2 = random.uniform(*SENSOR_RANGES["co2_level"])
    return GreenhouseSensorData(temp, humid, light, soil_m, co2)

def control_watering(sensor_data):
    """
    Applies fuzzy AI logic for watering control.
    """
    watering_action = "No action"

    # Rule 1: If soil moisture is < 35%, and either humidity is < 40% or temperature is > 30°C, initiate watering.
    if sensor_data.soil_moisture < 35:
        if sensor_data.humidity < 40 or sensor_data.temperature > 30:
            watering_action = "Initiate watering"
    # Rule 2: If soil moisture is between 35% and 50%, and temperature is > 35°C, initiate light watering.
    elif 35 <= sensor_data.soil_moisture <= 50 and sensor_data.temperature > 35:
        watering_action = "Initiate light watering"
    # Rule 3: If soil moisture is > 70%, skip watering.
    elif sensor_data.soil_moisture > 70:
        watering_action = "Skip watering (soil too wet)"

    return watering_action

def control_shading(sensor_data):
    """
    Uses a multiple-way selector (if-elif-else) for shading control.
    """
    shading_level = "No action"
    light = sensor_data.light_intensity

    if light < 300:
        shading_level = "Open shades (Very Low Light)"
    elif 300 <= light <= 800:
        shading_level = "No action (Moderate Light)"
    elif 800 < light <= 1000:
        shading_level = "Close partially (High Light)"
    elif light > 1000:
        shading_level = "Close fully (Very High Light)"

    return shading_level

def generate_alerts(sensor_data):
    """
    Implements a rule-based AI using logical conditions to generate alerts.
    Returns a tuple: (risk_alert_status, list_of_triggered_conditions)
    """
    triggered_conditions = []

    if sensor_data.temperature > 36:
        triggered_conditions.append("High Temp (>36°C)")
    if sensor_data.humidity < 25:
        triggered_conditions.append("Low Humidity (<25%)")
    if sensor_data.co2_level > 1200:
        triggered_conditions.append("High CO2 (>1200 ppm)")
    if sensor_data.soil_moisture < 30:
        triggered_conditions.append("Low Soil Moisture (<30%)")
    if sensor_data.light_intensity > 1100:
        triggered_conditions.append("Very High Light (>1100 lux)")

    risk_alert = len(triggered_conditions) >= 3
    return risk_alert, triggered_conditions

# --- Bonus: Mock AI Dashboard Functions ---

def calculate_moving_average(data_history, window):
    """Calculates the simple moving average for a given window."""
    if len(data_history) < window:
        return None
    return sum(list(data_history)[-window:]) / window

def display_dashboard(interval_num, historical_soil_moisture):
    """
    Logs actions and recommends future watering intervals based on trends.
    """
    print("\n--- AI Dashboard ---")
    print(f"Interval {interval_num} Summary:")

    # Trend analysis for soil moisture
    ma_soil = calculate_moving_average(historical_soil_moisture, MOVING_AVERAGE_WINDOW)
    if ma_soil is not None:
        print(f"  - Soil Moisture Moving Average ({MOVING_AVERAGE_WINDOW} intervals): {ma_soil:.1f}%")
        if ma_soil < 40: # Example threshold for recommendation
            print("  - Recommendation: Soil moisture trend is low. Consider proactive watering or checking irrigation system efficiency in upcoming intervals.")
        elif ma_soil > 65:
            print("  - Recommendation: Soil moisture trend is high. Monitor for potential overwatering in upcoming intervals.")
        else:
            print("  - Recommendation: Soil moisture trend is stable.")
    else:
        print(f"  - Not enough data for {MOVING_AVERAGE_WINDOW}-interval moving average yet.")
    print("--------------------")

# --- Main Simulation Loop ---

def main_simulation_loop():
    """
    Orchestrates the simulation over multiple intervals.
    """
    consecutive_alerts = 0
    historical_soil_moisture = deque(maxlen=MOVING_AVERAGE_WINDOW) # Stores last N soil moisture readings

    print("--- Smart Greenhouse Decision Support System Simulation ---")
    print(f"Simulating over {NUM_SIMULATION_INTERVALS} intervals (hours).\n")

    for i in range(1, NUM_SIMULATION_INTERVALS + 1):
        print(f"\n--- Interval {i} ---")

        # 1. Simulate real-time environmental input
        sensor_data = generate_sensor_data(i)
        print(f"Sensor Readings: {sensor_data}")
        historical_soil_moisture.append(sensor_data.soil_moisture)

        decision = GreenhouseDecision()

        # 2. Apply if-else, switch-case, and loops to control watering and shading
        decision.watering_action = control_watering(sensor_data)
        decision.shading_level = control_shading(sensor_data)

        # 3. Implement a rule-based AI using logical conditions and fuzzy thresholds to generate alerts
        decision.risk_alert, decision.alert_details = generate_alerts(sensor_data)

        # 4. Track consecutive alert states to escalate to a critical risk flag
        if decision.risk_alert:
            consecutive_alerts += 1
            if consecutive_alerts > 2:
                decision.critical_risk_flag = True
        else:
            consecutive_alerts = 0 # Reset if no alert

        # 5. Display system decisions and recommendations for each interval
        print(f"System Decisions:\n{decision}")

        # Bonus: Display mock AI dashboard
        display_dashboard(i, historical_soil_moisture)

    print("\n--- Simulation Complete ---")

# Run the simulation
if __name__ == "__main__":
    main_simulation_loop()
