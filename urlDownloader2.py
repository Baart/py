import urllib2
import shutil
#import urlparse
import os
import sys

def downloadFile(url):
	try:
		req = urllib2.urlopen(urllib2.Request(url))
	except Exception, e:
		print e, url
		return False
	
	filename = url.split("/").pop()
	size = int(req.info()["Content-length"])
	if size < 3000806:
		pass
		#print url, size
		with open("DL/"+filename, "wb") as f:
			shutil.copyfileobj(req, f)
	req.close()


def getUrlListFromFile(filename):
	result = []
	with open(filename, "r") as f:
		for line in f:
			result.append(line.rstrip(os.linesep))
	return result

def generateContentFile(url, output):
	req = urllib2.urlopen(urllib2.Request(url))
	result = []
	sub = req.read().split("<")
	for part in sub:
		if "href" in part.lower():
			content = part.split("\"")
			for subcontent in content:
				if "mp4"  in subcontent and "content" in subcontent:
					result.append(subcontent)

	with open(output, "w") as output:
		for line in result:
			output.write("http://o3hmi"+line+os.linesep)
	return result


linksfile = "myurllist.txt"

generateContentFile("http://o3hmi/content", linksfile) # extract links directly from webpage
links = getUrlListFromFile(linksfile)	# get array of links from generated file

for link in links:
	downloadFile(link)
