# PENETRATION-TESTING-TOOLKIT

**COMPANY**     : CODTECH IT SOLUTIONS

**NAME**        : SRIPADHI YASHWANTH

**INTERN ID**     : CT08HZS

**DOMAIN**     : CYBER SECURITY & ETHICAL HACKING

**BATCH DURATION**     : DECEMBER 30th, 2024 to JANUARY 30th, 2025

**MENTOR NAME**     : NEELA SANTHOSH KUMAR

#  DESCRIPTION

The given script implements a basic Penetration Testing Toolkit in Python. It contains three primary modules:

1)  Port Scanner:
-->  Scans specified ports on a target IP address to identify open ports.
-->  Uses threads to perform the scans in parallel, improving speed.

2)  Brute Forcer:
-->  Performs a brute-force attack on a target by trying combinations of a username and passwords from a provided wordlist.
-->  Simulates login attempts for educational purposes (you can integrate actual authentication mechanisms if allowed).

3)  Host Discovery:
-->  Identifies active hosts in a given network range by performing reverse DNS lookups.
-->  Simulates host discovery; could be extended with tools like ping or ICMP requests for more accuracy.

*  Description of Components:

1)  Initialization (__init__): Prints an initialization message when the toolkit is created.

2)  Port Scanner:
-->  Uses the socket module to attempt connections to specified ports.
-->  If the connection is successful (connect_ex returns 0), the port is identified as open.
-->  Implements threading to scan multiple ports concurrently.

3)  Brute Forcer:
-->  Reads passwords from a provided wordlist file and simulates login attempts.
-->  Currently, the actual login logic is replaced with a placeholder try_login function for demonstration.

4)  Host Discovery:
-->  Attempts to resolve hostnames for a range of IP addresses in the provided network prefix.
-->  Uses socket.gethostbyaddr to check for DNS records, indicating active hosts.

5)  Main Functionality:
-->  Presents a menu for the user to select one of the modules.
-->  Prompts for inputs relevant to the selected module (e.g., target IP, username, wordlist path).
-->  Executes the corresponding function of the toolkit.

*  Tools and Libraries

1)  socket (Built-in Library)
-->  Used for network-related operations, such as:
-->  Establishing connections to check if a port is open (port scanner).
-->  Performing reverse DNS lookups to identify active hosts (host discovery).
Functions used:
-->  socket.socket() – Creates a socket object.
-->  connect_ex() – Attempts to connect to a port, returning success or failure.
-->  gethostbyaddr() – Resolves an IP address to a hostname.

2)  itertools (Built-in Library)
-->  Not actively used in the code but often helpful for generating combinations or permutations, such as in brute force attacks.
-->  In this script, it is imported but unused.

3)  sys (Built-in Library)
-->  Used for interacting with the Python interpreter and handling system-level operations.
-->  In this script, it is imported but unused.

4)  threading.Thread (Built-in Library)
-->  Used to create and manage threads for concurrent execution.
-->  Enhances the performance of the Port Scanner by scanning multiple ports simultaneously.

#  OUTPUT

![Outputs](https://github.com/user-attachments/assets/67b60310-8d12-47ec-aea6-c98d45b23af3)

















