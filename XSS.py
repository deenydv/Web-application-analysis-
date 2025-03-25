import urllib.request

def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={urllib.parse.quote(payload)}"

    try:
        response = urllib.request.urlopen(test_url)
        content = response.read().decode()
        
        if payload in content:
            print(f"{RED}[VULNERABLE]{RESET} XSS detected at {url}")
        else:
            print(f"{GREEN}[SAFE]{RESET} No XSS found.")
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not connect to {url}")

test_xss("http://example.com/search"
