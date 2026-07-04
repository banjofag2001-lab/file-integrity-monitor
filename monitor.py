import os
import hashlib
import json


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    return hashlib.sha256(file_data).hexdigest()


def save_hashes(hashes):
    with open("hashes.json", "w") as file:
        json.dump(hashes, file, indent=4)


def load_hashes():
    if os.path.exists("hashes.json"):
        with open("hashes.json", "r") as file:
            return json.load(file)

    return {}


def scan_folder(folder_path):
    print("=" * 50)
    print("Security File Integrity Monitor")
    print("=" * 50)
    print("\nScanning folder...\n")

    old_hashes = load_hashes()
    new_hashes = {}

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        file_hash = calculate_hash(file_path)

        new_hashes[file_name] = file_hash

        if file_name not in old_hashes:
            print(f"NEW FILE DETECTED: {file_name}")

        elif old_hashes[file_name] != file_hash:
            print(f"WARNING: {file_name} has been modified!")

        else:
            print(f"OK: {file_name} has not changed")

    save_hashes(new_hashes)

    print("\nScan completed.")


def main():
    folder = "test_files"
    scan_folder(folder)


if __name__ == "__main__":
    main()