GridSense

Intelligent Energy Management System


Project Synopsis 

A smart energy management system called GridSense mimics how homes can effectively manage electricity in settings with erratic power sources.

As the primary client controller, the system intelligently coordinates various energy sources:

- Grid power (ZESA)
- Solar energy
- Battery storage
- Alternative fuel (generator)

It continuously monitors and adjusts energy usage to maintain stability and efficiency.


Objective

To design an intelligent energy management system that demonstrates the following advantages:

- Reduce dependence on unpredictable grid power.
- Use renewable energy as efficiently as possible.
- Verify the availability of power.
- Cut back on fuel consumption.


 Key Features

- Simulation in real time with updates every three seconds
- Time-based solar energy production (day versus night)
- Grid availability is unpredictable (load shedding   simulation).
- Dynamic discharging and charging of batteries
- The wise use of fuel only when required
- A loop of continuous monitoring


System Logic

•Solar Behavior

- 06:00 – 17:00: MEDIUM or HIGH output
- Night: LOW output

•Grid Power (ZESA)

- More likely to be OFF than ON to simulate outages

•Battery System

- Does not charge when:
  
  - Grid is OFF
  - Solar is LOW

- Charges when:
  
  - Solar is HIGH

- Maintained within safe limits (20% – 100%)

•Fuel Usage

Fuel is only consumed when:

- Grid is OFF
- Solar is LOW
- Battery is below 40%



Technologies Used

- Python 3
- "random" module (simulation logic)
- "time" module (real-time updates)


 How to Run

1. Install Python or use Pydroid
2. Clone or download this repository
3. Run the program:

python sensor.py

4. The system will continuously output live energy data.



 Role: Person B (Simulation Developer)

As Person B, I was responsible for:

- Designing and implementing the core simulation logic
- Developing realistic energy behavior (solar, grid, battery, fuel)
- Improving system efficiency and decision-making logic
- Testing and debugging the application
- Managing version control and updates on GitHub



 Future Improvements

-  Add a graphical dashboard (UI)
-  Integrate real IoT sensor data
-  Implement alert systems (low battery warnings)
-  Store historical data for analysis



Real-World Relevance

GridSense addresses real challenges faced in regions with:

- Frequent power outages such as Zimbabwe 
- High fuel costs
- Increasing reliance on solar energy

It demonstrates how intelligent systems can improve energy reliability and sustainability.


License

This project is for educational purposes, competitive purposes and demonstration purposes.