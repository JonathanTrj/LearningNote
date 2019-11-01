import requests
import re
import os

def first_test():
	r = requests.get("https://www.baidu.com")
	print(type(r))
	print(r.status_code)
	print(type(r.text))
	print(r.text)
	print(r.cookies)

# normal use of get()
def get_test1():
	r = requests.get("http://httpbin.org/get")
	print(r.text)
	
# pass params when using get()
def get_test2():
	data = {
		'name': 'germery',
		'age': 20
	}
	r = requests.get("http://httpbin.org/get", params = data)
	# print str
	print(r.text)
	# transfer to dict; Because the response string is in json format
	print(r.json())

# practice 1: zhihu
def get_test3():
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
	}
	r = requests.get("https://www.zhihu.com/explore", headers = headers)
	pattern = re.compile("<a.*?class=\"ExploreSpecialCard-banner\".*?><img.*?></a>", re.S)
	titles = re.findall(pattern, r.text)
	print(titles)

# practice 2: github favicon
def get_test4():
	r = requests.get("https://github.com/favicon.ico")
	print(r.text)
	print(r.content)
	with open(os.path.join(r"E:\trj\learnGit\Python\爬虫","github_favicon.ico"),'wb') as f:
		f.write(r.content)

# normal use of post()
def post_test():
	data = {
		'name': 'jonaehan',
		'age': 20
	}
	r = requests.post("http://httpbin.org/post", data=data)
	print(r.text)
	print(type(r.status_code), r.status_code)
	print(type(r.headers), r.headers)
	print(type(r.cookies), r.cookies)
	print(type(r.url), r.url)
	print(type(r.history), r.history)
	exit() if not r.status_code == requests.codes.ok else print("successfully")

# advance--post() upload file
def post_test1():
	files = {
		'file': open(os.path.join(r"E:\trj\learnGit\Python\爬虫", "requests_demo.py"), encoding="utf-8")
	}
	r = requests.post("http://httpbin.org/post", files=files)
	print(r.text)

# advance--post() cookies
def post_test2():
	headers = {
		'cookies': '...'
	}
	r = requests.post("https://www.baidu.com")
	print(r.cookies)
	for key, value in r.cookies.items():
		print(key + "=" + value)

# advance--keep session
def requests_test():
	# two diff requests can access the same data -- keep session
	requests.get("http://httpbin.org/cookies/set/number/123456789")
	r = requests.get("http://httpbin.org/cookies")
	print(r.text)	# print no cookie

	s = requests.Session()
	s.get("http://httpbin.org/cookies/set/number/123456789")
	r = s.get("http://httpbin.org/cookies")
	print(r.text)

if __name__ == "__main__":
	requests_test()