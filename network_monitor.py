import socket
import psutil
import datetime
import os

LOG_FILE = "network_monitor.log"

def log_message(message):
    """Append message to log file with timestamp."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def get_tcp_connections():
    """Retrieve active TCP connections."""
    connections = psutil.net_connections(kind="tcp")
    log_message("Active TCP Connections:")
    for conn in connections:
        if conn.laddr and conn.raddr:
            log_message(
                f"Local: {conn.laddr.ip}:{conn.laddr.port} -> "
                f"Remote: {conn.raddr.ip}:{conn.raddr.port} | Status: {conn.status}"
            )
    return connections

def resolve_dns(domain):
    """Perform DNS lookup for a given domain."""
    try:
        ip = socket.gethostbyname(domain)
        log_message(f"DNS Resolution: {domain} -> {ip}")
        return ip
    except socket.gaierror as e:
        log_message(f"DNS Resolution Error for {domain}: {str(e)}")
        return None

def main():
    """Main function to monitor network and log results."""
    log_message("Starting Network Monitoring Tool")
    get_tcp_connections()
    domains = ["google.com", "akamai.com", "invalid.domain"]
    for domain in domains:
        resolve_dns(domain)
    log_message("Monitoring Complete")

if __name__ == "__main__":
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    main()