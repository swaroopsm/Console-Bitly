#!/usr/bin/python
import urllib
import urllib2
import json
import settings as s

class ConsoleBitly:
	def shorten(self,req):
		url="http://api.bitly.com/v3/shorten?login="+s.bitly_username+"&apiKey="+s.bitly_apikey+"&longUrl="+req
		print "Please wait... \n"
		response=urllib2.urlopen(url)
		a = json.loads(response.read())
		print "\nShortened URL is: \033[1;36m"+a['data']['url']+"\033[1;m\n"


c=ConsoleBitly()
req=raw_input("Enter the URL to be shortened: ")
c.shorten(req)

