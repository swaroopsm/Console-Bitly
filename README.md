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
		bitly.shorten("http://google.com")
		
		#### URL Expand ####
		bitly.expand("http://bit.ly/VaYjPq")
		
		#### URL Information ####
		bitly.info("http://bit.ly/VaYjPq")
		
		#### Lookup for a URL ####
		bitly.info("http://google.com")
