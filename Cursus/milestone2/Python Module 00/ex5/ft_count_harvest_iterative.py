def ft_count_harvest_iterative():
    count: int = 1
    day: int = int(input("Days until harvest: "))
    if count > day:
        return
    while day >= count:
        print("Day", count)
        count += 1
    print("Harvest time!")
