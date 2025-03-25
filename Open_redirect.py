import urllib.request

def check_open_redirect(url):
    payload = "/redirect?url=http://evil.com"
    test_url = url + payload

    try:
        response = urllib.request.urlopen(test_url)
        if "evil.com" in response.geturl():
            print(f"{RED}[VULNERABLE]{RESET} Open redirect detected at {url}")
        else:
            print(f"{GREEN}[SAFE]{RESET} No open redirect found.")
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not connect to {url}")

check_open_redirect("http://example.com"
