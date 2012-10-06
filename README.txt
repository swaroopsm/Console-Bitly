Console-Bitly:
	A thin wrapper for the bit.ly API.
		
Quick Install:
	sudo pip install git+git://github.com/swaroopsm/Console-Bitly.git
		
Usage:
	from ConsoleBitly import ConsoleBitly
	bitly_username="YOUR_BITLY_USERNAME"
	bitly_apikey="YOUR_BITLY_API_KEY"
	bitly=ConsoleBitly(bitly_username,bitly_apikey)
		
	#### API METHODS ####
		
	#### URL Shorten ####
		if bitly.shorten("http://google.com"):
			bitly['value']
		
	#### URL Expand ####
		if bitly.expand("http://bit.ly/VaYjPq"):
			bitly['value']
		
	#### URL Information ####
		if bitly.info("http://bit.ly/VaYjPq"):
			bitly['value']
		
	#### Lookup for a URL ####
		if bitly.info("http://google.com"):
			bitly['value']
