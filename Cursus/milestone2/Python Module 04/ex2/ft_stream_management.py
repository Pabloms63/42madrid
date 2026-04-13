import sys
import typing


def recover_data(file_name: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    print("---\n")
    file_handle: typing.IO

    try:
        file_handle = open(file_name, "r")
        data = file_handle.read()
        file_handle.close()
        print(data, end="")

        print("\n---")
        print(f"File '{file_name}' closed.\n")

        print("Transform data:")
        transformed_data = data.replace('\n', '#\n')
        if data and not data.endswith('\n'):
            transformed_data += '#\n'
        print("---\n")

        print(transformed_data, end="")

        print("\n---")
        sys.stdout.write("\nEnter new file name (or empty): ")
        sys.stdout.flush()

        new_name = sys.stdin.readline().strip()
        if not new_name:
            print("Not saving data.")
        else:
            try:
                print(f"Saving data to '{new_name}'")
                write_handle = open(new_name, 'w')
                write_handle.write(transformed_data)
                write_handle.close()
                print(f"Data saved in file '{new_name}'.")
            except (PermissionError, FileNotFoundError) as e:
                sys.stderr.write(
                    f"[STDERR] Opening file '{new_name}' as {e}\n")
                print("Data not saved.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"[STDERR] Error opening file {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        recover_data(sys.argv[1])
