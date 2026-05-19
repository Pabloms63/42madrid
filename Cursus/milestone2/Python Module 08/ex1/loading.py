import importlib.metadata


def check_dependencies() -> bool:
    packages = ["pandas", "numpy", "matplotlib"]

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


def analyze_matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix_data = np.random.randn(1000)

    df = pd.DataFrame(matrix_data, columns=['Matrix stream'])

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(df, color='green')
    plt.title("Matrix Data Analysis")

    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_dependencies():
        analyze_matrix()
