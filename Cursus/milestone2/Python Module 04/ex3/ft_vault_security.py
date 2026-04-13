def secure_archive(file_name: str, act: int, string: str = "") -> (True | False, str):
    try:
        if act == 1:
            with open(file_name, "r") as f:
                content = f.read()
            return (True, content)
        elif act == 2:
            with open(file_name, "w") as w:
                w.write(string)
            return (True, "Content successfully written to file")
        return (False, "Invalid action requested")
    except (FileNotFoundError, PermissionError) as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 1))

    print("\nUsing 'secure_archive' to read from an inaccessible bfile:")
    print(secure_archive('/etc/master.passwd', 1))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("text.txt", 1))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text2.txt", 2, "Content successfully written to file"))
