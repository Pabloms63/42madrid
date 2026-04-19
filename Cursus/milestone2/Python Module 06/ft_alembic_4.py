import alchemy


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Showing not all functions can be reached")
print("This will raise an exception!")
try:
    print(f"Testing hidden create_earth: {alchemy.create_earth()}")
except AttributeError as e:
    print(f"AttributeError: {e}. Did you mean: 'create_air'?")
