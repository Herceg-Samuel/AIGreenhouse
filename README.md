Designing a Rule-Based AI for Smart Greenhouse Decision Support System Scenario: In a semi-arid region of Kenya, a cooperative of small-scale farmers is adopting AI-assisted greenhouse farming to improve food production.
Your team has been hired to develop the core logic module of the Smart Greenhouse Decision Support System (SGDSS), which uses sensor data to make real-time decisions on irrigation, shading, and alert generation based on predefined expert rules.

The system receives hourly input from environmental sensors:

- Temperature (°C)
- Humidity (%)
- Light Intensity (lux)
- Soil Moisture (%)
- CO₂ Level (ppm)

The AI component is based on rule-based reasoning and simple fuzzy logic thresholds that simulate “human-like” decision-making in uncertain conditions.

🔍 Requirements and Constraints
•
Watering Control (Fuzzy AI Logic):
•
If soil moisture is < 35%, and either humidity is < 40% or temperature is > 30°C, initiate watering.
•
If soil moisture is between 35% and 50%, and temperature is > 35°C, initiate light watering.
•
If soil moisture is > 70%, skip watering.
•
Shading Control:
•
Use a multiple-way selector (e.g., switch-case) to categorize light levels:
•
Very Low (<300 lux): Open shades.
•
Moderate (300–800 lux): No action.
•
High (800–1000 lux): Close partially.
•
Very High (>1000 lux): Close fully.

AI-Driven Risk Alerts:
•
Raise alerts if 3 or more of the following hold true:
•
Temperature > 36°C
•
Humidity < 25%
•
CO₂ > 1200 ppm
•
Soil moisture < 30%
•
Light intensity > 1100 lux
•
If alerts are triggered for more than 2 consecutive intervals, raise a Critical Risk Flag.
•
Simulation Loop:
•
Simulate sensor input and decision-making logic over 10 intervals (e.g., hours).
•
Allow random or pre-defined sensor input values.
•
Output system decisions (watering, shading level, risk alert, and critical flag) at each step.
🛠️ Task
Write a modular high-level code or pseudo-code to: 1. Simulate real-time environmental input over 10 intervals. 2. Apply if-else, switch-case, and loops to control watering and shading. 3. Implement a rule-based AI using logical conditions and fuzzy thresholds to generate alerts. 4. Track consecutive alert states to escalate to a critical risk flag. 5. Display system decisions and recommendations for each interval.
🚀 Bonus (Optional - 5 Marks)
Connect the system to a mock AI dashboard that logs actions and recommends future watering intervals based on trends (simulate using moving average of soil moisture).
