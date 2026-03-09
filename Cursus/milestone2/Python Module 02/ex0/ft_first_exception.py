def check_temperature(temp):
    try:
        temp = int(temp)
        print(f"\nTesting temperature: {temp}")
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"\nTesting temperature: {temp}")
        print(f"Error: '{temp}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    check_temperature(25)
    check_temperature("bcd")
    check_temperature(456)
    check_temperature(-34)
    print("\nAll tests completed - program didn't crash!")
