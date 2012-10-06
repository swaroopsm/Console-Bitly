## Console-Bitly
		A thin wrapper for the bit.ly API.
		
### Quick Install
		sudo pip install git+git://github.com/swaroopsm/Console-Bitly.git
		
### Usage
		from ConsoleBitly import ConsoleBitly
		bitly_username="YOUR_BITLY_USERNAME"
		bitly_apikey="YOUR_BITLY_API_KEY"
		bitly=ConsoleBitly(bitly_username,bitly_apikey)
		
		#### API METHODS ####
		
		#### URL Shorten ####
		s = bitly.shorten("http://google.com")
		if s['success']: print s['value']
		
		#### URL Expand ####
		e = bitly.expand("http://bit.ly/VaYjPq")
		if e['success']: print e['value']
		
		#### URL Information ####
		i = bitly.info("http://bit.ly/VaYjPq")
		if i['success']: print i['value']
		
		#### Lookup for a URL ####
		l = bitly.info("http://google.com")
		if l['success']: print l['value']
