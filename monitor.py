import os
import hashlib


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    return hashlib.sha256(file_data).hexdigest()


def scan_folder(folder_path):
    print("=" * 50)
    print("Security File Integrity Monitor")
    print("=" * 50)
    print("\nScanning folder...\n")

    print(f"Folder: {folder_path}\n")

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        file_hash = calculate_hash(file_path)

        print(f"Found: {file_name}")
        print(f"SHA-256: {file_hash}\n")

    print("Scan completed.")


def main():
    folder = "test_files"
    scan_folder(folder)


if __name__ == "__main__":
    main()