def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    new_file = "new_discovery.txt"
    print(f"Initializing new storage unit: {new_file}")

    try:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        file = open(new_file, "w")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{new_file}' ready for long-term preservation.")
    except Exception:
        print("ERROR: Failed to create storage unit.")


if __name__ == "__main__":
    main()
