import urllib, re, os

url = "https://brickset.com/sets/year-2020"
content = urllib.urlopen(url).read()
# print("content\n" + content)
keyword = "</span>\s[A-Z|a-z|\s|'|&|.]+"
m = re.findall(keyword, content)
# _ = os.system('clear')
# print(m)
if m:
	for part in m:
		print(part[8:])
else:
	print("Could not found")