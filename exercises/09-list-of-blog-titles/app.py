import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
#response = requests.get(url)
#json = response.json()

def get_titles():
    titles = []
    response = requests.get(url)
    json = response.json()
    posts = json['posts']
    posts_titles = [ p["title"] for p in posts]
    return posts_titles


print(get_titles())
