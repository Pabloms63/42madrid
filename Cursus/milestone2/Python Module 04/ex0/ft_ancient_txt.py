def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    vault_file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {vault_file}")

    try:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        vault = open(vault_file, "r")
        data = vault.read()
        print(data)
        vault.close()
        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
