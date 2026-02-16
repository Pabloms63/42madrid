def ft_water_reminder():
    days_water: int = int(input("Days since last watering: "))
    if days_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
