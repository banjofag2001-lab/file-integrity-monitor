import os


def scan_folder(folder_path):
    print("=" * 50)
    print("Security File Integrity Monitor")
    print("=" * 50)
    print("\nScanning folder...\n")

    print(f"Folder: {folder_path}\n")

    for file_name in os.listdir(folder_path):
        print(f"Found: {file_name}")
        print("\nScan completed.")


def main():
    folder = "test_files"
    scan_folder(folder)


if __name__ == "__main__":
    main()