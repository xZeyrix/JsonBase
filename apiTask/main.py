import httpx

url="https://jsonplaceholder.typicode.com/users"

response = httpx.get(url)
data = response.json()

# Task 1
for user in data:
    print(user["name"], user["email"])

# Task 2
for user in data:
    if user["id"] == 5:
        print(user)

# Task 3
print(len(data))

# Task 4
for user in data:
    print(user["username"])