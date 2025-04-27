#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' 

separator() {
    echo -e "${CYAN}--------------------------------------------${NC}"
}

show_banner() {
    separator
    echo -e "${GREEN}Linux System Information Script${NC}"
    separator
}

os_info() {
    separator
    echo -e "${YELLOW}Operating System Info:${NC}"
    lsb_release -a 2>/dev/null || cat /etc/os-release
    uname -a
}

cpu_info() {
    separator
    echo -e "${YELLOW}CPU Info:${NC}"
    lscpu | grep -E "Model name|Architecture|CPU\(s\)"
}

memory_info() {
    separator
    echo -e "${YELLOW}Memory Info:${NC}"
    free -h
}

disk_info() {
    separator
    echo -e "${YELLOW}Disk Usage:${NC}"
    df -h --total | grep total
}

uptime_info() {
    separator
    echo -e "${YELLOW}System Uptime:${NC}"
    uptime -p
}

user_info() {
    separator
    echo -e "${YELLOW}Logged-in Users:${NC}"
    who
}

network_info() {
    separator
    echo -e "${YELLOW}Network Info:${NC}"
    ip a | grep inet
}

process_info() {
    separator
    echo -e "${YELLOW}Top Processes by CPU Usage:${NC}"
    ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -10
}

last_logins() {
    separator
    echo -e "${YELLOW}Last Logins:${NC}"
    last -n 5
}

services_status() {
    separator
    echo -e "${YELLOW}Some Important Services:${NC}"
    systemctl is-active sshd 2>/dev/null && echo "SSHD: Active" || echo "SSHD: Inactive"
    systemctl is-active docker 2>/dev/null && echo "Docker: Active" || echo "Docker: Inactive"
    systemctl is-active ufw 2>/dev/null && echo "Firewall (UFW): Active" || echo "Firewall (UFW): Inactive"
}

running_services() {
    separator
    echo -e "${YELLOW}Running Services:${NC}"
    systemctl list-units --type=service --state=running | head -20
}

kernel_info() {
    separator
    echo -e "${YELLOW}Kernel Version:${NC}"
    uname -r
}

temp_info() {
    separator
    echo -e "${YELLOW}Temperature Info:${NC}"
    sensors 2>/dev/null || echo "Temperature sensors not available."
}

public_ip_info() {
    separator
    echo -e "${YELLOW}Public IP Address:${NC}"
    curl -s ifconfig.me || echo "Unable to fetch Public IP."
}

firewall_status() {
    separator
    echo -e "${YELLOW}Firewall Status:${NC}"
    sudo ufw status verbose 2>/dev/null || echo "UFW not installed or inactive."
}

clear
show_banner

os_info
cpu_info
memory_info
disk_info
uptime_info
user_info
network_info
kernel_info
process_info
last_logins
services_status
running_services
temp_info
public_ip_info
firewall_status

separator
echo -e "${GREEN}System information gathering complete.${NC}"
separator
