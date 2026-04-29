import importlib.metadata

def check_dependencies() -> bool:
    packages = ["pandas", "numpy", "requests", "matplotlib"]

    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    
    all_ok = True
    for p in packages:
        try:
            version = importlib.metadata.version(p)
            print(f"[OK] {p} ({version})")
        except importlib.metadata.PackageNotFoundError:
            print(f"[ERROR] Missing dependency: {p}")
            all_ok = False

    if not all_ok:
        print("Install with Pip: pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        return False
    return True


def analyze_matrix():
    print("Analyzing Matrix data...")


if __name__ == "__main__":
    if check_dependencies():
        analyze_matrix()
