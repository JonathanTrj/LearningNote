from urllib import parse
from urllib import request

url = "http://httpbin.org/post"
headers = {
	'User-Agent': "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
	'Host': 'httpbin.org'
}
dict = {
	'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url = url, data = data, headers = headers, method = "POST")
res = request.urlopen(req)
print(res.read().decode("utf-8"))