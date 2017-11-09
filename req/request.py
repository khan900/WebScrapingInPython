import requests

try:
	obj = requests.get('http://www.gutenberg.org/cache/epub/98/pg98.txt')
	obj.raise_for_status()
	fhandle = open('A Tale of Two Cities.txt','wb')
	for data in obj.iter_content(100000):
		fhandle.write(data)
except Exception as x:
	print('There was a problem: %s' %(x))

fhandle.close()

