import urllib.request

def test_sql_injection(url):
    payload = "' OR '1'='1"
    test_url = f"{url}?id={urllib.parse.quote(payload)}"

    try:
        response = urllib.request.urlopen(test_url)
        content = response.read().decode()
        
        if "mysql" in content.lower() or "syntax error" in content.lower():
            print(f"{RED}[VULNERABLE]{RESET} SQL Injection detected at {url}")
        else:
            print(f"{GREEN}[SAFE]{RESET} No SQL injection found.")
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not connect to {url}")

test_sql_injection("http://example.com/search"
