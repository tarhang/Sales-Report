import requests

with requests.session() as sess:
    url = "https://squareup.com/ca/en"
    response = sess.get(url)
    print(response.text)
