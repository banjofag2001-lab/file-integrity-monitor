# File Integrity Monitor

A Python cybersecurity automation tool that monitors files for unauthorized changes using SHA-256 hashing.

## Overview

File Integrity Monitor helps detect file changes by creating cryptographic fingerprints of files and comparing them during future scans.

The tool can detect:
- New files added
- Modified files
- Deleted files

This demonstrates a core cybersecurity concept used in system monitoring and threat detection.

## Features

- Scan directories for files
- Generate SHA-256 file hashes
- Store file fingerprints using JSON
- Compare previous and current file states
- Detect unauthorized modifications
- Detect new files
- Detect deleted files
- Generate security scan reports
- Send email alerts when changes are detected
- Run easily on Windows using a launcher script
- Secure credentials using environment variables
## Technologies Used

- Python
- Hashlib
- JSON
- OS module
- Datetime module
- SMTP email automation
- Python-dotenv
- Git and GitHub

## Project Structure

```
file-integrity-monitor/

├── monitor.py
├── email_alert.py
├── hashes.json
├── README.md
├── requirements.txt
├── run_monitor.bat
├── .gitignore
├── reports/
└── test_files/
```
## Example Output
Security File Integrity Monitor

OK: notes.txt unchanged

WARNING: password.txt modified

NEW FILE DETECTED: example.txt

ALERT: old_file.txt deleted

Report generated.
Scan completed.

## Skills Demonstrated

- Python programming
- Cybersecurity automation
- File integrity monitoring
- Hash generation
- Working with JSON data
- File handling
- Basic threat detection logic
- Version control using Git

## Future Improvements

- Add email security alerts
- Add real-time file monitoring
- Create a dashboard interface
- Add log analysis features

## Purpose

This project was created to practice security automation concepts and demonstrate how Python can be used to build cybersecurity monitoring tools.