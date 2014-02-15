from flask import Flask

import sys

app = Flask(__name__)

def extract_pseudo(line):
	line = line.split()
	pseudo = line[4]
	pseudo = pseudo.split(":")[1]
	pseudo = pseudo.split("(")[0]
	return pseudo


def read_murmur():
	''' Return an array of pseudo of connected people '''
	connected    = []
	with open("murmur.log") as f:
		for line in f:
			if "Authenticated" in line:
				pseudo = extract_pseudo(line)
				if(pseudo not in connected):
					connected.append(pseudo)
					#print (pseudo, "connected")
			if "closed" in line:
				pseudo = extract_pseudo(line)
				if(pseudo in connected):
					connected.remove(pseudo)
					#print (pseudo, "disconnected")
	
	return connected




@app.route("/")
def hello():
	page = "<div>"
	for pseudo in read_murmur():
		page += "<a>" + pseudo + " is connected</a>" 
	page += "</div>"
	return page

if __name__ == "__main__":
	app.run(host="0.0.0.0")
