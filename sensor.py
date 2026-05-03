import random
import time

battery = 70
fuel = 100

def get_sensor_data():
    global battery, fuel

    hour = time.localtime().tm_hour

    # Solar pattern
    if 6 <= hour <= 17:
        solar = random.choice(["MEDIUM", "HIGH"])
    else:
        solar = "LOW"

    # ZESA (more OFF than ON)
    grid = "OFF" if random.random() < 0.7 else "ON"

    # Battery behavior
    if grid == "OFF" and solar == "LOW":
        battery -= random.randint(2, 5)
    elif solar == "HIGH":
        battery += random.randint(1, 3)

    battery = max(20, min(100, battery))

    # Fuel usage (only when needed)
    if grid == "OFF" and solar == "LOW" and battery < 40:
        fuel -= random.randint(2, 6)

    fuel = max(0, fuel)

    return {
        "battery": battery,
        "solar": solar,
        "grid": grid,
        "fuel": fuel,
        "time": time.strftime("%H:%M:%S")
    }


if __name__ == "__main__":
    while True:
        print(get_sensor_data())
        time.sleep(3)