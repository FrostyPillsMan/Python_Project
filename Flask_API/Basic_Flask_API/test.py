import requests

URL_BASE = "http://127.0.0.1:5000/"


payload = [
    {"name": "Give it up", "views": 100000, "likes": 20000},
    {"name": "HeartBreaker", "views": 210000, "likes": 15000},
    {"name": "All at Once", "views": 30000, "likes": 20500}
]

payload_2 = {}

# URL-encoded path

response = requests.patch(URL_BASE + "music/2", json=payload_2, headers={"Content-Type": "application/json"})
print(response.json())

"""
for i in range(len(payload)):
    response = requests.put(URL_BASE + "music/" + str(i), json=payload[i])
    if response.status_code == 201:
        print(f"Created: {response.json()}")
    else:
        print(f"Failed to create music {i}: {response.status_code}, {response.text}")
"""
        
# input("Press Enter to continue...")

# Corrected URL for deletion
# response = requests.delete(URL_BASE + "music/0")
# print(response)

# input("Press Enter to continue...")

# Corrected URL for getting
# response = requests.get(URL_BASE + "music/6")

# Check if the response was successful

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, Response: {response.text}")

