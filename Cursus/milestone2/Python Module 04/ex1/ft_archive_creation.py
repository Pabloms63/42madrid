import sys
import typing


def recover_data(file_name: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file {file_name}")
    file_handle: typing.IO
    print("---\n")

    try:
        file_handle = open(file_name, "r")
        data = file_handle.read()
        print(data, end="")
        file_handle.close()

        print("\n---")
        print(f"File '{file_name}' closed.")

        print("\nTransfom data:")
        print("---")

        transformed_data = data.replace('\n', '#\n')
        print(transformed_data, end="")
        
        print("\n---")
        new_name = input("Enter new file name (or empty):")
        if not new_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            write_handle = open(new_name, "w")
            write_handle.write(transformed_data)
            write_handle.close()
            print(f"Data saved in file '{new_name}'")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {file_name}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        recover_data(sys.argv[1])
