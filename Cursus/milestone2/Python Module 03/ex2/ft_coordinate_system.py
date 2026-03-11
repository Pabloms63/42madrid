import sys
import math

print("=== Game Coordinate System ===\n")

if len(sys.argv) == 4:
	coordinates = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
	print(f"Position created: ({coordinates[0]}, {coordinates[1]}, {coordinates[2]})")
	distance = math.sqrt(((coordinates[0] - 0)**2) + ((coordinates[1] - 0)**2) + ((coordinates[2] - 0)**2))
	print(f"Distance between: (0, 0, 0) and {coordinates}: {int(distance)}")
else:
	print("Error: Arguments have to be 4.")
