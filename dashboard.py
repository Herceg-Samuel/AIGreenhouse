# Import the main greenhouse control system
from main import watering

# Mock AI Dashboard and Trend Analysis
from datetime import datetime, timedelta
import time

class GreenHouseDashboard:
    def __init__(self):
        self.moisture_history = []
        self.action_log = []
        self.window_size = 3  # Size of moving average window
    
    def log_action(self, action, readings):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.action_log.append(f"{timestamp}: {action}")
        self.moisture_history.append(readings['moisture'])
        
    def get_moisture_trend(self):
        if len(self.moisture_history) >= self.window_size:
            recent_moisture = self.moisture_history[-self.window_size:]
            avg_moisture = sum(recent_moisture) / len(recent_moisture)
            trend = "stable"
            if avg_moisture < 0.35:
                trend = "decreasing"
            elif avg_moisture > 0.6:
                trend = "increasing"
            return trend, avg_moisture
        return "insufficient data", 0
    
    def recommend_watering(self):
        trend, avg_moisture = self.get_moisture_trend()
        if trend == "insufficient data":
            return "Collecting more data..."
        
        if trend == "decreasing":
            return "WARNING: Soil getting dry. Schedule watering soon!"
        elif trend == "increasing":
            return "Soil moisture trending up. No immediate watering needed."
        else:
            return "Soil moisture stable. Continue regular monitoring."

def run_simulation():
    # Simple simulation
    print("\n=== Smart Greenhouse AI Dashboard Simulation ===")
    dashboard = GreenHouseDashboard()

    # Simulate 6 readings over time
    test_conditions = [
        # moisture, temp, humidity - simulating drying trend
        (0.65, 28, 0.5),  # Start with wet soil
        (0.55, 30, 0.45), # Gradually drying
        (0.45, 32, 0.4),  # Still drying
        (0.32, 34, 0.35), # Getting dry
        (0.28, 35, 0.3),  # Very dry
        (0.25, 36, 0.25)  # Critically dry
    ]

    print("\nStarting simulation with readings every 2 seconds...")
    for i, (moisture, temp, hum) in enumerate(test_conditions, 1):
        print(f"\nInterval {i} - Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"Moisture: {moisture:.2f}, Temp: {temp}°C, Humidity: {hum:.2f}")
        
        # Get system's watering decision
        print("\nSystem Decision:")
        watering(moisture, temp, hum)
        
        # Log the readings and get AI recommendations
        dashboard.log_action(
            f"Readings: Moisture={moisture:.2f}, Temp={temp}°C, Humidity={hum:.2f}", 
            {'moisture': moisture}
        )
        
        print("\nAI Dashboard Analysis:")
        trend, avg = dashboard.get_moisture_trend()
        if trend != "insufficient data":
            print(f"Moisture Trend: {trend}")
            print(f"Moving Average: {avg:.2f}")
        print(f"Recommendation: {dashboard.recommend_watering()}")
        
        # Show recent action log
        print("\nRecent Actions:")
        for log in dashboard.action_log[-3:]:  # Show last 3 actions
            print(log)
        
        print("-" * 50)
        time.sleep(2)  # Simulate time passing

    print("\nSimulation complete!")

if __name__ == "__main__":
    run_simulation()
