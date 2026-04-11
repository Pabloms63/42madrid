import sys, os, site


def is_virtual_env():
    return sys.prefix != sys.base_prefix

def main():
    if is_virtual_env():
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        env_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        packages = site.getsitepackages()
        if packages:
            print("\nPackage installation path:")
            print(packages[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows")


if __name__ == "__main__":
    main()
