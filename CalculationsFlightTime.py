def calculate_flight_time(battery_capacity_mAh, battery_voltage, motor_current_A, num_motors, draw_fraction=1.0, usable_fraction=0.8):
    battery_wh = (battery_capacity_mAh / 1000) * battery_voltage * usable_fraction
    total_current = motor_current_A * draw_fraction * num_motors
    power_w = total_current * battery_voltage
    if power_w == 0:
        return 0
    time_min = (battery_wh / power_w) * 60
    return round(time_min, 2)

def main():
    print("=== Drone Flight Time Estimator ===")
    battery_capacity_mAh = float(input("Battery capacity (mAh): "))
    battery_voltage = float(input("Battery voltage (V): "))
    motor_current_A = float(input("Max motor current (A): "))
    num_motors = int(input("Number of motors: "))
    draw_fraction = float(input("Draw fraction (e.g. 0.4 for hover): ") or 1.0)
    usable_fraction = float(input("Usable battery fraction (default 0.8): ") or 0.8)

    time = calculate_flight_time(
        battery_capacity_mAh,
        battery_voltage,
        motor_current_A,
        num_motors,
        draw_fraction,
        usable_fraction
    )

    print(f"\nEstimated Flight Time: {time} minutes")

if __name__ == "__main__":
    main()
