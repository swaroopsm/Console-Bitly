#!/usr/bin/python
import urllib
import urllib2
import json

class ConsoleBitly:
	def __init__(self,bitly_username,bitly_apikey):
		self.bitly_username=bitly_username
		self.bitly_apikey=bitly_apikey
		
	def shorten(self,req):
		try:
			url="http://api.bitly.com/v3/shorten?login="+self.bitly_username+"&apiKey="+self.bitly_apikey+"&longUrl="+req
			print "Please wait... \n"
			response=urllib2.urlopen(url)
			a = json.loads(response.read())
			print "\nShortened URL is: \033[1;36m"+a['data']['url']+"\033[1;m\n"
		except:
			print "\033[1;31mThe provided url may be invalid. Prefix URL with http OR https...\033[1;m\n"
	
	def expand(self,req):
		try:
			url="http://api.bitly.com/v3/expand?login="+self.bitly_username+"&apiKey="+self.bitly_apikey+"&shortUrl="+req
			print "Please wait... \n"
			response=urllib2.urlopen(url)
			a = json.loads(response.read())
			print "\nExpanded URL is: \033[1;36m"+a['data']['expand'][0]['long_url']+"\033[1;m\n"
		except:
			print "\033[1;31mThe provided url might not be of a bit.ly domain OR shortened version does not exist!\033[1;m\n"
	
	def info(self,req):
		try:
			url="http://api.bitly.com/v3/info?login="+self.bitly_username+"&apiKey="+self.bitly_apikey+"&shortUrl="+req
			print "Please wait... \n"
			response=urllib2.urlopen(url)
			a = json.loads(response.read())
			title=str(a['data']['info'][0]['title'])
			if title=='None':
				print "\nExpanded URL is: \033[1;36m There exists 'NO TITLE' for this URL.\033[1;m\n"
			else:
				print "\nExpanded URL is: \033[1;36m"+title+"\033[1;m\n"
		except:
			print "Invalid bitly shortened URL"
			
	def lookup(self,req):
		url="http://api.bitly.com/v3/lookup?login="+self.bitly_username+"&apiKey="+self.bitly_apikey+"&url="+req
		print "Please wait... \n"
		response=urllib2.urlopen(url)
		a = json.loads(response.read())
		try:
			url=str(a['data']['lookup'][0]['short_url'])
			print "\nLookup URL is: \033[1;36m"+url+"\033[1;m\n"
		except:
			print "\n\033[1;31m Either the lookup does not exist or you forgot to add a trailing slash at the end of the URL\033[1;m\n"
	
