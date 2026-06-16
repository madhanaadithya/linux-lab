import subprocess

def run(cmd):
    return subprocess.getoutput(cmd)

print("=== NET DOCTOR (PYTHON) ===\n")

# Local IP
ip = run("ip route get 1.1.1.1 | awk '{print $7; exit}'")
print("Local IP:", ip)

# Gateway
gw = run("ip route | awk '/default/ {print $3}'")
print("Gateway:", gw)

print("\nDNS TEST:")
dns = run("getent hosts google.com")
print("OK" if dns else "FAIL")

print("\nINTERNET TEST:")
ping = run("ping -c 1 8.8.8.8")
print("OK" if "1 received" in ping else "FAIL")

print("\nOPEN PORTS:")
ports = run("ss -tulpn | grep LISTEN")
print(ports if ports else "No open ports found")
