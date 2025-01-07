import socket
import itertools
import sys
from threading import Thread

class PenetrationTestingToolkit:

    def __init__(self):
        print("\nPenetration Testing Toolkit Initialized\n")

    # Port Scanner
    def port_scanner(self, target, ports):
        print(f"\nStarting Port Scan on {target}\n")

        def scan_port(port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)
                    result = s.connect_ex((target, port))
                    if result == 0:
                        print(f"[+] Port {port} is open")
            except socket.error:
                print(f"[-] Error scanning port {port}")

        threads = []
        for port in ports:
            thread = Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    # Brute Forcer
    def brute_forcer(self, target, username, wordlist):
        print(f"\nStarting Brute Force Attack on {target}\n")

        def try_login(password):
            # Simulate a login attempt (replace with actual login code)
            print(f"Trying: {username}:{password.strip()}")

        with open(wordlist, 'r') as file:
            passwords = file.readlines()

        for password in passwords:
            try_login(password)

    # Basic Host Discovery
    def host_discovery(self, network):
        print(f"\nStarting Host Discovery on {network}\n")
        
        def ping_host(ip):
            try:
                response = socket.gethostbyaddr(ip)
                print(f"[+] Host discovered: {ip} - {response[0]}")
            except socket.error:
                pass

        # Simulate discovering hosts (use a valid network scanner in production)
        for i in range(1, 5):
            ip = f"{network}.{i}"
            ping_host(ip)

if __name__ == "__main__":
    toolkit = PenetrationTestingToolkit()

    print("Modules Available:")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("3. Host Discovery")

    choice = input("Select a module: ")

    if choice == "1":
        target = input("Enter target IP: ")
        ports = range(1, 101)  # Scans ports 1-100
        toolkit.port_scanner(target, ports)

    elif choice == "2":
        target = input("Enter target service: ")
        username = input("Enter username: ")
        wordlist = input("Enter path to wordlist: ")
        toolkit.brute_forcer(target, username, wordlist)

    elif choice == "3":
        network = input("Enter network prefix (e.g., 192.168.1): ")
        toolkit.host_discovery(network)

    else:
        print("Invalid choice.")
