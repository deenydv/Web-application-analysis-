import urllib.request

def check_directory_listing(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        
        if "<title>Index of" in content:
            print(f"{RED}[VULNERABLE]{RESET} Directory listing enabled at {url}")
        else:
            print(f"{GREEN}[SAFE]{RESET} No directory listing exposure.")
    except:
        print(f"{YELLOW}[ERROR]{RESET} Could not connect to {url}")

check_directory_listing("http://example.com/uploads/"
