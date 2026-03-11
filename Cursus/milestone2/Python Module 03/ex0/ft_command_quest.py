import sys

print("=== Command Quest ===")

if len(sys.argv) < 2:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {len(sys.argv) - 1}")
    for i, arg in enumerate(sys.argv):
        if i == 0:
            pass
        else:
            print(f"Argument {i}: {arg}")
print(f"Total arguments: {len(sys.argv)}")
