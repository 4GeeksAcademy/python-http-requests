import requests

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_post_tags(post_id):
    response = requests.get(url)
    json = response.json()
    posts = {}
    for p in json['posts']:
        if p['id'] == post_id:
            return p['tags']

print(get_post_tags(146))