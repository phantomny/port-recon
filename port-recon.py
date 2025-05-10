import socket
import threading

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP: ")
    ports = range(1, 1025)
    threads = []

    print(f"[*] Scanning {target}...\n")
    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("[*] Scan complete.")

if __name__ == "__main__":
    main()
