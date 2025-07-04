import socket
import json
import sys
from datetime import datetime

def validate_input(host, start_port, end_port):
    """Validate user input for host and port range."""
    try:
        socket.inet_aton(host)  # Check if host is a valid IP
        if not (1 <= start_port <= end_port <= 65535):
            raise ValueError("Port range must be between 1 and 65535.")
        return True
    except socket.error:
        print("Invalid IP address.")
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False

def scan_port(host, port):
    """Scan a single port on the host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1-second timeout
        result = sock.connect_ex((host, port))
        sock.close()
        return port, result == 0  # Return port and True if open, False if closed
    except Exception as e:
        return port, False

def save_results(results, filename="scan_results.json"):
    """Save scan results to a JSON file."""
    try:
        scan_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "host": results["host"],
            "open_ports": results["open_ports"]
        }
        with open(filename, "w") as f:
            json.dump(scan_data, f, indent=4)
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    """Main function to run the port scanner."""
    print("Simple Port Scanner")
    host = input("Enter target IP address: ").strip()
    try:
        start_port = int(input("Enter start port (1-65535): ").strip())
        end_port = int(input("Enter end port (1-65535): ").strip())
    except ValueError:
        print("Ports must be numbers.")
        return

    if not validate_input(host, start_port, end_port):
        return

    print(f"Scanning {host} from port {start_port} to {end_port}...")
    results = {"host": host, "open_ports": []}

    for port in range(start_port, end_port + 1):
        port, is_open = scan_port(host, port)
        if is_open:
            results["open_ports"].append(port)
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

    if results["open_ports"]:
        print("\nOpen ports:", results["open_ports"])
    else:
        print("\nNo open ports found.")

    save_results(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)