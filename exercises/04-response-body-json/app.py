import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
#print(response.text)

json_r = response.json()
#print(json_r["hours"])

print(f"Current time:", (json_r["hours"]), "hrs", (json_r["minutes"]), "min and", (json_r["seconds"]), "sec")
