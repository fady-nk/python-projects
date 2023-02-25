import requests

proxies = {"http":"183.82.116.56:8080"} #type the ip of the proxy
headers = {"user-agent*": "Chrome/7.0(x11 ; linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"} # edit your user agent

r = requests.get("http://example.com/whoami", proxies=proxies,headers=headers)
print(r.text)
for cookie in r.cookies:
    print(cookie)
print(r.cookies["TestinggGround"])
