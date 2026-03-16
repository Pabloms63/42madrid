import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")

    inventory = {}
    for arg in sys.argv[1:]:
        name, amount = arg.split(":")
        amount = int(amount)
        inventory[name] = amount

    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique items types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for item, amount in inventory.items():
        percentage = (amount / total) * 100
        print(f"{item}: {amount} units ({round(percentage, 1)}%)")

    print("\n=== Inventory Statistics ===")
    max_amount = 0
    for item, amount in inventory.items():
        if amount > max_amount:
            key_max = item
            max_amount = amount

    print(f"Most abundant: {key_max} ({max_amount} units)")

    min_amount = max_amount
    for item, amount in inventory.items():
        if amount < min_amount:
            key_min = item
            min_amount = amount

    print(f"Most abundant: {key_min} ({min_amount} units)")

    print("\n=== Item Categories ===")
    scarces = {}
    moderates = {}
    for item, amount in inventory.items():
        if amount <= 4:
            scarces.update({item: amount})
        if amount >= 5 and amount <= 10:
            moderates.update({item: amount})

    print(f"Moderate: {moderates}")
    print(f"Scarces: {scarces}")

    print("\n=== Management Suggestions ===")
    restock_needed = {}
    for item, amount in inventory.items():
        if amount <= 1:
            restock_needed.update({item: amount})

    print(f"Restock needed: {', '.join(restock_needed.keys())}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(
        f"Dictionary values: "
        f"{', '.join(str(value) for value in inventory.values())}"
        )
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
