from django.shortcuts import render


def home(request):
	import requests
	import json

	'''1.grab crypto price data of BTC,ETH,BCH,EOS,ETC,LTC,XRP,TRX,NEO,DASH
	in INR
	   2. grab latest crypto currency news in english  (english and portugal were available)

	'''
	#grab crypto price
	price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,EOS,ETC,LTC,XRP,TRX,NEO,DASH&tsyms=INR')
	price = json.loads(price_request.content)

	#grab crypto news
	api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api':api,'price':price})



def prices(request):
	'''
	we are passing single currency code or multiple currency codes seperated by commas and no space which will be used
	to find their details through api
	currently displaying
	Name,Price, daily high, daily low 
	'''
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+ quote +'&tsyms=INR')
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote,'crypto':crypto})

	else:	
		notfound = "You need to enter the crypto currency symbol to get quote."
		return render(request, 'prices.html', {'notfound': notfound})