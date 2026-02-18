def ft_count_harvest_recursive(day=None, count=1):
    if day is None:
        day = int(input("Days until harvest: "))
    if count > day:
        return
    print("Day", count)
    ft_count_harvest_recursive(day, count + 1)
    if day == count:
        print("Harvest time!")
