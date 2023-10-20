import requests
name = input('Enter the name you want:')
r = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/{0}".format(name))
page = r.json()
print(page["extract"])