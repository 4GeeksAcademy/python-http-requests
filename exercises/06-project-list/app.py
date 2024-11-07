import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
json = response.json()
print(json[1]["name"])