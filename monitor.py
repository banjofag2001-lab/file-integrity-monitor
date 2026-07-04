import os
import hashlib
import json
from datetime import datetime
from email_alert import send_email_alert


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


def save_report(results):
    os.makedirs("reports", exist_ok=True)

    file_name = datetime.now().strftime(
        "reports/security_report_%Y%m%d_%H%M%S.txt"
    )

    with open(file_name, "w") as file:
        file.write("Security Scan Report\n")
        file.write("=" * 30 + "\n\n")

        file.write(
            "Scan Time: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n\n"
        )

        for result in results:
            file.write(result + "\n")


def scan_folder(folder_path):
    print("=" * 50)
    print("Security File Integrity Monitor")
    print("=" * 50)

    old_hashes = load_hashes()
    new_hashes = {}

    results = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        file_hash = calculate_hash(file_path)

        new_hashes[file_name] = file_hash


        if file_name not in old_hashes:
            message = f"NEW FILE DETECTED: {file_name}"


        elif old_hashes[file_name] != file_hash:
            message = f"WARNING: {file_name} modified"


        else:
            message = f"OK: {file_name} unchanged"


        print(message)
        results.append(message)


    for old_file in old_hashes:
        if old_file not in new_hashes:
            message = f"ALERT: {old_file} deleted"

            print(message)
            results.append(message)


    save_hashes(new_hashes)

    save_report(results)


    alerts = []

    for result in results:
        if (
            "WARNING" in result
            or "ALERT" in result
            or "NEW FILE" in result
        ):
            alerts.append(result)


    if alerts:
        send_email_alert(alerts)
        print("Email alert sent.")


    print("\nReport generated.")
    print("Scan completed.")


def main():
    folder = "test_files"
    scan_folder(folder)


if __name__ == "__main__":
    main()