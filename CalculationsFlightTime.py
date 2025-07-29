
def calculate_flight_time_by_weight(
    battery_capacity_mAh,
    battery_voltage,
    motor_max_current_A,
    motor_max_thrust_g,
    drone_weight_g,
    num_motors,
    usable_fraction=0.8
):
    # Calculate battery energy
    battery_wh = (battery_capacity_mAh / 1000) * battery_voltage * usable_fraction

    # Estimate hover current based on thrust-to-weight
    thrust_per_motor = motor_max_thrust_g
    required_thrust_per_motor = drone_weight_g / num_motors
    hover_fraction = required_thrust_per_motor / thrust_per_motor

    hover_current_per_motor = motor_max_current_A * hover_fraction
    total_current = hover_current_per_motor * num_motors

    power_w = total_current * battery_voltage
    if power_w <= 0:
        return 0

    time_min = (battery_wh / power_w) * 60
    return round(time_min, 2)

def main():
    print("=== Drone Flight Time Estimator (Weight-Based) ===")
    battery_capacity_mAh = float(input("Battery capacity (mAh): "))
    battery_voltage = float(input("Battery voltage (V): "))
    motor_max_current_A = float(input("Motor max current (A): "))
    motor_max_thrust_g = float(input("Motor max thrust (g): "))
    num_motors = int(input("Number of motors: "))
    drone_weight_g = float(input("Total drone weight (g): "))
    usable_fraction = float(input("Usable battery fraction (default 0.8): ") or 0.8)

    time = calculate_flight_time_by_weight(
        battery_capacity_mAh,
        battery_voltage,
        motor_max_current_A,
        motor_max_thrust_g,
        drone_weight_g,
        num_motors,
        usable_fraction
    )

    print(f"\nEstimated Flight Time: {time} minutes")

if __name__ == "__main__":
    main()
