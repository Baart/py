from flask import Flask

import sys
import os

app = Flask(__name__)

def extract_pseudo(line, log_file):
	
	line = line.split()
	#print (line)
	if "murmur" in log_file:
		pseudo = line[4]
		if ":" in pseudo:
			pseudo = pseudo.split(":")[1]
			pseudo = pseudo.split("(")[0]
	if "minecraft" in log_file:
		pseudo = line[3]
	return pseudo


def read_murmur(log_file, join, left):
	''' Return an array of pseudo of connected people '''
	connected    = []
	with open(log_file) as f:
		for line in f:
			if join in line:
				pseudo = extract_pseudo(line, log_file)
				if(pseudo not in connected):
					connected.append(pseudo)
					#print (pseudo, "connected")
			if left in line:
				pseudo = extract_pseudo(line, log_file)
				if(pseudo in connected):
					connected.remove(pseudo)
					#print (pseudo, "disconnected")
	
	return connected

def get_html_connected(connected, service):
	page = "<div><br>"+service+"<br>"
	if not connected:
		page += "<a>Personne sur "+service+"</a>"
	for pseudo in connected:
		page += "<a>" + pseudo + " is connected</a><br>" 
	page += "</div>"
	return page

	

def read_logs():
	page = ""
	connected = read_murmur("murmur.log", "Authenticated", "closed")
	page += get_html_connected(connected, "Mumble")

	connected = read_murmur("minecraft.log", "joined", "left")
	page += get_html_connected(connected, "Minecraft")
	return page
	
def print_backups():
	page = "<div>"
	array = os.listdir("/home/ws/backup_minecraft")
	page = "<br>".join(array)
	page += "</div>"
	return page



@app.route("/")
def hello():
	page = read_logs()
	page += "<br><div><a>Minecrafts backups<a><br>"
	page += print_backups()
	page += "</div>"
	return page

	
if __name__ == "__main__":
	app.run(host="0.0.0.0")
	#read_logs()
