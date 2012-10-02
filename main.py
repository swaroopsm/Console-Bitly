#!/usr/bin/python
import urllib
import urllib2
import json
import settings as s

req=raw_input("Enter the URL to be shortened: ")
url="http://api.bitly.com/v3/shorten?login="+s.bitly_username+"&apiKey="+s.bitly_apikey+"&longUrl="+req
response=urllib2.urlopen(url)
a = json.loads(response.read())
print a['data']['hash']
