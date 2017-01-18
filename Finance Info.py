#program 

import subprocess
import json
import requests
import time

# program

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']
 
def get_value(identifier):
	get_value_url = 'http://finance.google.com/finance/info?client=ig&q=' + identifier 
	value = subprocess.Popen(['curl', '-s', get_value_url], stdout=subprocess.PIPE).communicate()[0]
	j = json.loads(value[5:len(value)-2])
	return float(j['l'])
 
if __name__ == "__main__":
	stockname = raw_input("Please enter stalk symbol: ")
	#inputformat =  'NASDAQ:AAPL'
	print "USER INPUT: " + stockname
	companycode = stockname.split(":")[1]
	share_value = get_value(stockname)
	companyname = get_symbol(companycode)
	localtime = time.asctime( time.localtime(time.time()) )
	print companyname
	print localtime
	print stockname 
	print share_value
	#finish
