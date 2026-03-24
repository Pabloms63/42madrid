def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    # EXTRACCIÓN (LECTURA)
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")

            data = file.read()
            print(data.strip())

    except FileNotFoundError:
        print("[ERROR] classified_data.txt not found")
        data = ""

    # PRESERVACIÓN (LECTURA + ESCRITURA)
    try:
        with open("security_protocols.txt", "r") as file:
            print("\nSECURE PRESERVATION:")

            protocols = file.read()
            print(protocols.strip())

        # AQUÍ USAS WRITE (clave)
        with open("vault_log.txt", "w") as log:
            log.write(data)
            log.write("\n")
            log.write(protocols)

    except FileNotFoundError:
        print("[ERROR] security_protocols.txt not found")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
