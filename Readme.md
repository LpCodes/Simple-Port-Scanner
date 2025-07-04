# Simple Port Scanner

A lightweight Python-based port scanner for cybersecurity reconnaissance. Scans a target IP for open ports within a specified range and saves results to a JSON file. Ideal for learning about network security and ethical hacking.

## Features

Scans a target IP for open ports in a user-defined range
Saves scan results to scan_results.json
Basic input validation for IP and port range
Simple, procedural code without classes
Handles interruptions gracefully

##  Requirements

Python 3.6+
No external dependencies

##  Installation

Clone the repository:git clone <your-repo-url>
cd port-scanner


Run the script:python port_scanner.py



## Usage
Run the script and follow the prompts:

Enter the target IP address (e.g., 192.168.1.1 or a public IP like scanme.nmap.org for testing).
Specify the start and end ports (e.g., 1-1024).
The scanner will check each port and report if it’s open or closed.
Results are saved to scan_results.json.

## Important: Only scan hosts you have permission to test. Unauthorized scanning may be illegal.
Example
$ python port_scanner.py
Simple Port Scanner
Enter target IP address: scanme.nmap.org
Enter start port (1-65535): 20
Enter end port (1-65535): 80
Scanning scanme.nmap.org from port 20 to 80...
Port 20: CLOSED
Port 21: CLOSED
Port 22: OPEN
Port 23: CLOSED
...
Port 80: OPEN

Open ports: [22, 80]
Results saved to scan_results.json

##  Contributing
Feel free to fork the repository and submit pull requests for improvements, such as adding multi-threading, custom port lists, or enhanced output formats.

## License
MIT License

## Disclaimer
This tool is for educational purposes only. Use it responsibly and only on systems you have explicit permission to scan. Unauthorized port scanning is illegal in many jurisdictions.