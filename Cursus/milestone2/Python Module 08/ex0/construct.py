import sys
import os
import site


def check_matrix() -> None:
    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment:  None detected")
        print("\nARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without affectingthe global system."
        )
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])


if __name__ == "__main__":
    check_matrix()
