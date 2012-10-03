#!/usr/bin/python
import urllib
import urllib2
import json
import settings as s

class ConsoleBitly:
	@staticmethod
	def shorten(req,self=None):
		try:
			url="http://api.bitly.com/v3/shorten?login="+s.bitly_username+"&apiKey="+s.bitly_apikey+"&longUrl="+req
			print "Please wait... \n"
			response=urllib2.urlopen(url)
			a = json.loads(response.read())
			print "\nShortened URL is: \033[1;36m"+a['data']['url']+"\033[1;m\n"
		except:
			print "\033[1;31mThe provided url may be invalid. Prefix URL with http OR https...\033[1;m\n"
	
	@staticmethod	
	def expand(req,self=None):
		try:
			url="http://api.bitly.com/v3/expand?login="+s.bitly_username+"&apiKey="+s.bitly_apikey+"&shortUrl="+req
			print "Please wait... \n"
			response=urllib2.urlopen(url)
			a = json.loads(response.read())
			print "\nExpanded URL is: \033[1;36m"+a['data']['expand'][0]['long_url']+"\033[1;m\n"
		except:
			print "\033[1;31mThe provided url might not be of a bit.ly domain OR shortened version does not exist!\033[1;m\n"
	
	@staticmethod
	def info(req,self=None):
		try:
			url="http://api.bitly.com/v3/info?login="+s.bitly_username+"&apiKey="+s.bitly_apikey+"&shortUrl="+req
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
	
