def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
