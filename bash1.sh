#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

separator() {
    echo -e "${CYAN}--------------------------------------------${NC}"
}

banner() {
    separator
    echo -e "${GREEN}OSINT Recon Script${NC}"
    echo -e "${GREEN}By ChatGPT 🕵️‍♂️${NC}"
    separator
}

whois_lookup() {
    separator
    echo -e "${YELLOW}WHOIS Information:${NC}"
    whois "$TARGET" 2>/dev/null || echo "WHOIS lookup failed."
}

dns_lookup() {
    separator
    echo -e "${YELLOW}DNS Information:${NC}"
    dig "$TARGET" ANY +noall +answer || echo "DNS lookup failed."
}

geoip_lookup() {
    separator
    echo -e "${YELLOW}IP Geolocation:${NC}"
    IP=$(dig +short "$TARGET" | tail -n1)
    if [[ -z "$IP" ]]; then
        echo "Failed to get IP address."
    else
        curl -s "https://ipinfo.io/${IP}/json" | jq
    fi
}

screenshot_website() {
    separator
    echo -e "${YELLOW}Website Screenshot (Optional):${NC}"
    if command -v chromium &> /dev/null; then
        chromium --headless --disable-gpu --screenshot --window-size=1280,800 "http://${TARGET}"
        echo "Screenshot saved as screenshot.png"
    else
        echo "Chromium not installed. Skipping screenshot."
    fi
}

search_social_media() {
    separator
    echo -e "${YELLOW}Social Media Search (Google Dorks):${NC}"
    echo "Searching for: $TARGET"
    echo "Twitter mentions:"
    echo "https://twitter.com/search?q=$TARGET"
    echo
    echo "Instagram posts:"
    echo "https://www.instagram.com/explore/tags/$TARGET/"
    echo
    echo "GitHub search:"
    echo "https://github.com/search?q=$TARGET"
}

reverse_whois_lookup() {
    separator
    echo -e "${YELLOW}Reverse WHOIS / Historical Data (manual lookup):${NC}"
    echo "Try looking up at:"
    echo "https://viewdns.info/reversewhois/?q=$TARGET"
    echo "https://securitytrails.com/domain/$TARGET/history"
}

email_hunting() {
    separator
    echo -e "${YELLOW}Email Pattern Hunting:${NC}"
    echo "Try hunting emails for domain $TARGET at:"
    echo "https://hunter.io/search/$TARGET"
}

# ========== MAIN ==========

clear
banner

read -p "Enter target domain or username (no http/https): " TARGET

if [[ -z "$TARGET" ]]; then
    echo -e "${RED}No target provided. Exiting.${NC}"
    exit 1
fi

whois_lookup
dns_lookup
geoip_lookup
search_social_media
reverse_whois_lookup
email_hunting

read -p "Do you want to take a website screenshot? (y/n): " SS
if [[ "$SS" == "y" || "$SS" == "Y" ]]; then
    screenshot_website
else
    echo "Skipping website screenshot."
fi

separator
echo -e "${GREEN}Recon complete!${NC}"
separator
