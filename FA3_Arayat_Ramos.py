
from abc import ABC, abstractmethod

# Abstract Base Class
class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


# Child Class: pH Sensor
class PHSensor(Sensor):
    def __init__(self, reading):
        self.reading = reading

    def get_reading(self):
        return f"{self.reading} pH (Neutral)"


# Child Class: Temperature Sensor
class TempSensor(Sensor):
    def __init__(self, reading):
        self.reading = reading

    def get_reading(self):
        return f"{self.reading}°C"


# Main Program
def main():
    print("--- Lab Inventory System ---")

    # Create sensor objects
    ph_sensor = PHSensor(7.2)
    temp_sensor = TempSensor(24.5)

    # Display sensor readings
    print(f"[pH Sensor] Reading: {ph_sensor.get_reading()}")
    print(f"[Temperature Sensor] Reading: {temp_sensor.get_reading()}")
    print("------------------------------")
    
    my_sensor = Sensor()


if __name__ == "__main__":
    main()
