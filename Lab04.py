import random
import time
import threading
import sys

# Global data structures
latest_temperatures = {}
temperature_averages = {}
lock = threading.RLock()

def simulate_sensor(sensor_id):
    """Simulate temperature readings from a sensor and update global dictionary."""
    global latest_temperatures
    while True:
        temp = random.randint(15, 40)  # Generate a random temperature between 15 and 40
        with lock:
            latest_temperatures[sensor_id] = temp
        time.sleep(1)  # Update every second

def process_temperatures():
    """Continuously calculate the average temperature every 5 seconds."""
    global temperature_averages
    while True:
        with lock:
            for sensor_id, temp in latest_temperatures.items():
                if sensor_id in temperature_averages:
                    # Simple moving average: (previous_avg * 4 + new_temp) / 5
                    temperature_averages[sensor_id] = (temperature_averages[sensor_id] * 4 + temp) / 5
                else:
                    temperature_averages[sensor_id] = temp  # Initialize average
        time.sleep(5)  # Update every 5 seconds

def initialize_display(sensor_count):
    """Initialize display layout with placeholders for temperature values."""

    spaces = " "*30
    
    display_lines = []

    display_lines.append("Current temperatures:")

    latest_line = "Latest Temperatures: " + " ".join([f"Sensor {i}: --\u00b0C" for i in range(sensor_count)])
    display_lines.append(latest_line)

    for i in range(sensor_count):
        display_lines.append(f"Sensor {i+1} Average: {spaces} --\u00b0C")
    
    sys.stdout.write("\n".join(display_lines) + "\n")
    sys.stdout.flush()  # Ensure everything is printed out correctly


def move_cursor_up(n=1):
    """Move the cursor up by 'n' lines."""
    sys.stdout.write(f"\033[{n}A")
    sys.stdout.flush()

def update_display(sensor_count):
    """Update the display in place without erasing the console, replacing '--' with real data."""
    line_count = sensor_count + 2  # Latest temp + sensor averages + heading
    
    while True:
        with lock:
            # Move cursor up to overwrite previous data
            move_cursor_up(line_count)

            spaces = " "*30

            print("Current temperatures:")

            # Latest Temperatures
            latest_temps = "Latest Temperatures: " + " ".join([
                f"Sensor {i}: {latest_temperatures.get(i, '--')}\u00b0C" for i in range(sensor_count)
            ])
            print(latest_temps)

            # Average Temperatures
            for i in range(sensor_count):
                avg = f"{temperature_averages.get(i, '--'):.2f}" if i in temperature_averages else '--'
                print(f"Sensor {i+1} Average: {spaces} {avg}\u00b0C")

        time.sleep(1)  # Refresh the display every second


def main():
    sensor_count = 3  # Number of sensors
    initialize_display(sensor_count)

    time.sleep(5)

    # Start sensor threads
    sensor_threads = []
    for i in range(sensor_count):
        thread = threading.Thread(target=simulate_sensor, args=(i,), daemon=True)
        sensor_threads.append(thread)
        thread.start()
    
    # Start data processing thread
    process_thread = threading.Thread(target=process_temperatures, daemon=True)
    process_thread.start()
    
    # Start display thread
    display_thread = threading.Thread(target=update_display, args=(sensor_count,), daemon=True)
    display_thread.start()
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Temperature Monitoring System terminated.")


if __name__ == "__main__":
    main()



# 4. Questions:
# 1) Why did the professor not ask you to compute metrics?
# Answer: I think the main aim of this lab is for me to learn how to manage concurrent tasks, use threads, locks, and synchronize shared resources efficiently.

"""
4. Questions:

1) Why did the professor not ask you to compute metrics?

Answer: 
I think the main aim of this lab is for me to learn how to manage concurrent tasks,
use threads, locks, and synchronize shared resources efficiently.

"""