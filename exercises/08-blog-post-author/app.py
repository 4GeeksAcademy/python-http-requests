import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
json = response.json()

#print(json)

print(json["posts"][0]["author"]["name"])