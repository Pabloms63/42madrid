def ft_count_harvest_iterative():
    count: int = 0
    day: int = int(input("Days until harvest: "))
    if count > day:
        return
    while day >= count:
        print("Day ", count)
        count += 1
