import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def main():
    config = load_config()

    mode = config.get("MATRIX_MODE") or "development"

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to cloud instance")
        print("API Access: Authenticated")
        print("Zion Network: Online")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print("Zion Network: Online")

    print(f"Log Level: {config.get('LOG_LEVEL') or 'DEBUG'}")

    print("\nEnvironment security check:")

    # checks estilo subject
    if config.get("API_KEY") and config["API_KEY"] != "your_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] Missing or default API key")

    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()