import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)

json = response.json()
#print(json)
print(json["name"])