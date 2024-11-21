import httpx

r = httpx.get('https://api.github.com/user', auth=('user', 'pass'))

print(f"Status Code: {r.status_code}")

print(f"Content: {r.content}")

print(f"Headers: {r.headers['content-type']}")

print(f"Encoding: {r.encoding}")

print(f"Json: {r.json()}")


