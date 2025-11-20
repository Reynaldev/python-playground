import requests

response = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")

print(response.status_code)
print(response.content)
