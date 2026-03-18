if __name__ == "__main__":
	print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
	vault_file = "ancient_fragment.txt"
	print(f"Accessing storage Vault: {vault_file}")

	try:
		vault = open(vault_file, "r")
		print("Connection established...")

		data =vault.read()
		print("RECOVERED DATA:")
		print(data)

		vault.close()
		print("\nData recovery complete. Storage unit disconnected.")
	except FileNotFoundError:
		print("ERROR: Storage vault not found.")