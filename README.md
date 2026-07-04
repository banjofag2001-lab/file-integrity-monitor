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
- Detect deleted files
- Generate security scan reports

## Technologies Used

- Python
- Hashlib
- JSON
- OS module
- Git

## Project Structure

```
file-integrity-monitor/

├── monitor.py
├── hashes.json
├── README.md
├── requirements.txt
├── reports/
└── test_files/
```

1. The program scans files inside the monitored folder.
2. It generates a SHA-256 hash for each file.
3. The hashes are stored as a baseline.
4. On future scans, new hashes are compared with previous hashes.
5. Any file changes are detected and reported.

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