import requests
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

def get_attachment_by_id(attachment_id):
    response = requests.get(url)
    data = response.json()
    for post in data['posts']:
        for attach in post['attachments']:
            if attach['id'] == attachment_id:
                return attach['title']
            

    return None

print(get_attachment_by_id(137))