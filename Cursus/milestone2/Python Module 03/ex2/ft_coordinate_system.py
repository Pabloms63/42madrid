import sys
import math

print("=== Game Coordinate System ===\n")

if len(sys.argv) == 1:
    coordinates = (10, 20, 5)
    print(f"Position created: {coordinates}")

    distance = math.sqrt((coordinates[0]**2) + (coordinates[1]**2) + (coordinates[2]**2))
    print(f"Distance between: (0, 0, 0) and {coordinates}: {round(distance, 2)}")

    coord_string = "3,4,0"
    print(f'\nParsing coordinates: "{coord_string}"')

    try:
        parsed = tuple(map(int, coord_string.split(",")))
        print(f"Parsed position: {parsed}")

        distance2 = math.sqrt((parsed[0]**2) + (parsed[1]**2) + (parsed[2]**2))
        print(f"Distance between: (0, 0, 0) and {parsed}:  {distance2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    invalid_string = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: {invalid_string}")
    try:
        parsed_invalid = tuple(map(int, invalid_string.split(",")))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    
    print("\nUnpacking demonstration:")
    print(f"Player at x={parsed[0]}, y={parsed[1]}, z={parsed[2]}")
    print(f"Coordinates: X={parsed[0]}, Y={parsed[1]}, Z={parsed[2]}")
else:
    print("Error: This program does not take arguments.")
