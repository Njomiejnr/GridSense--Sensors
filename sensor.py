import random
import time

def get_sensor_data():
    hour = time.localtime().tm_hour

    # Simulate solar based on time
    if 6 <= hour <= 17:
        solar = random.choice(["LOW", "MEDIUM", "HIGH"])
    else:
        solar = "LOW"

    # Simulate ZESA (random outages)
    grid = random.choice(["ON", "OFF"])

    # Battery level
    battery = random.randint(40, 90)

    # Fuel level
    fuel = random.randint(30, 100)

    return {
        "battery": battery,
        "solar": solar,
        "grid": grid,
        "fuel": fuel
    }


# Test it
if __name__ == "__main__":
    while True:
        print(get_sensor_data())
        time.sleep(3)