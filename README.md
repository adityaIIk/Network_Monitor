# Network Monitoring Tool

A Python-based tool to monitor TCP connections and DNS resolution on Linux, designed to identify network bottlenecks and optimize performance. This project demonstrates skills in Linux, networking protocols (TCP, DNS, HTTP/S), and troubleshooting, aligning with roles like Akamai's Associate Cloud Support Engineer.

## Features
- Monitors active TCP connections (local/remote IP, port, status).
- Performs DNS lookups for specified domains.
- Logs results to `network_monitor.log` for analysis.
- Supports Wireshark for HTTP/S traffic analysis to reduce latency.

## Prerequisites
- Linux system (e.g., Ubuntu 20.04+)
- Python 3.6+
- Required packages: `psutil`
- Optional: Wireshark for HTTP/S traffic analysis

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/adityaIIk/network_monitor.git
   cd network-monitor