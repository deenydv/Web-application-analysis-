import http.client

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def fetch_headers(domain):
    print(f"{BLUE}Checking security headers for {domain}...\n{RESET}")

    conn = http.client.HTTPSConnection(domain)
    conn.request("HEAD", "/")
    response = conn.getresponse()
    
    headers = dict(response.getheaders())
    security_headers = ["X-Frame-Options", "X-XSS-Protection", "Strict-Transport-Security", "Content-Security-Policy"]

    for header in security_headers:
        if header in headers:
            print(f"{GREEN}[SECURE]{RESET} {header}: {headers[header]}")
        else:
            print(f"{YELLOW}[MISSING]{RESET} {header} is missing!")

fetch_headers("example.com"
